from math import pi


class Column(object):
    '''
    geometry: [diameter cm, length cm]
    particle_size: diameter cm
    porosity: porosity of the column
    n_columns: number of columns default n_columns=1
    A: cross-section area cm**2
    Dm: diffusion coufficient cm**2/sec
    norm_velocity: normalized velocity -
    
    '''
    def __init__(self, geometry, particle_size, porosity, Pump, n_columns=1, CFL=0.35):
        self.CFL = CFL
        self.geometry = geometry
        self.particle_size = particle_size
        self.porosity = porosity
        self.n_columns = n_columns
        self.F = (1-self.porosity)/self.porosity
        self.A = (pi/4)*self.geometry[0]**2
        self.Dm = 10**(-5)
        self.velocity = Pump.volume_flow_sec/(self.A*self.porosity)
        self.norm_velocity = self.particle_size*self.velocity/self.Dm
        self.dz = (2/self.norm_velocity+self.norm_velocity**(1/3)+self.norm_velocity/10)*self.particle_size
        self.dt = self.dz/(self.CFL*self.velocity)