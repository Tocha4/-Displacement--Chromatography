

cdef (float, float) clc_komponenten(float inter,float cnij,float const,float q0ij,float const1_1,float const1,float c0ij,float F):
    cdef float q1ij = inter*cnij/const
    cdef float dq = q1ij-q0ij
    cdef float C1i1j = const1_1*cnij-const1*c0ij+F*dq
    return q1ij,C1i1j    


cpdef simulation_cython(int num_time_steps, int num_length_steps,
                        double[:] adsorption, double[:,:,:] C,
                        int num_components, double[:,:,:] q,
                        list inter, float const1_1,
                        float const1, float F): #(self.num_time_steps)
    cdef int m
    cdef int mm = len(adsorption)
    cdef int n
    cdef int i
    cdef int j
    cdef float const
    for n in range(1,num_time_steps-1):
        for i in range(0,num_length_steps-1):
            const = 1+sum([adsorption[m] * C[n,i,m] for m in range(mm)])                 #1+np.dot(adsorption, C[n,i,:])
            for j in range(num_components):
                q[n,i,j],C[n,i+1,j] = clc_komponenten(inter[j],C[n,i,j],const,q[n-1,i, j],const1_1,const1,C[n-1,i, j],F)
    return q,C
