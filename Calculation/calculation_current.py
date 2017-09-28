import numpy as np
import os 


if 'cytthon_functions' in os.listdir():
    from cytthon_functions import Functions
else:
    from Calculation.cytthon_functions import Functions
                                                              

class Simu():
    
    def __init__(self,Sample,Column,Interaction, Pump, time_factor=1 ):
        self.Interaction = Interaction
        self.Sample = Sample
        self.Column = Column
        self.Pump = Pump
        self.num_length_steps = int(Column.geometry[1]*Column.n_columns//Column.dz)
        self.num_time_steps = int((Column.geometry[1]*Column.n_columns//(Column.velocity*Column.dt))*time_factor)
        self.C = np.zeros([self.num_time_steps,self.num_length_steps,len(Sample.composition)])
        self.q = np.zeros([self.num_time_steps,self.num_length_steps,len(Sample.composition)])
        self.tinj = int(self.Sample.volume//(self.Pump.volume_flow_sec*self.Column.dt))
        self.num_components = range(len(self.Sample.composition))
        
    def injection(self):
        self.C[0:self.tinj, 0 , :] = np.array([np.array(self.Sample.composition)*self.Sample.concentration for _ in np.arange(self.tinj)])
        self.C[self.tinj:self.num_time_steps,0,:] = np.array([self.Sample.disp_concentration for _ in np.arange(self.num_time_steps-self.tinj)])

    def simulation(self):
        const1 = -(self.Column.dz/(self.Column.dt*self.Column.velocity))
        F = self.Column.F*const1
        const1_1 = 1+const1
        inter = list(self.Interaction.ads_max*self.Interaction.adsorption)
        qq, cc = Functions.simulation_cython(self.num_time_steps, self.num_length_steps,
                                             self.Interaction.adsorption,
                                             self.C,len(self.num_components),
                                             self.q,inter,const1_1,const1,F)
        self.q = np.array(qq)
        self.C = np.array(cc)
        return self.q,self.C
    
    def enable(self):
        del self.C,self.q
 
if __name__ == '__main__':
    
    pass
    
