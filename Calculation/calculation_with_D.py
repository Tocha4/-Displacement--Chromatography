import time
import numpy as np
from column_01 import Column 
from pump_01 import Pump
from sample_01 import Sample
from interaction_01 import Interaction
from calculation_current import Simu

import os
print(os.listdir())
if 'functions_with_D' in os.listdir():
    from functions_with_D import Functions
else:
    from Calculation.functions_with_D import Functions



class Simu_with_D(Simu):
    
    def simulation(self):
        const1 = -(self.Column.dz/(self.Column.dt*self.Column.velocity))
        F = self.Column.F*const1
        const1_1 = 1+const1
        inter = list(self.Interaction.ads_max*self.Interaction.adsorption)
        qq, cc = Functions.simulation_with_D(self.num_time_steps, self.num_length_steps,
                                             self.Interaction.adsorption,
                                             self.C,len(self.num_components),
                                             self.q,inter,const1_1,const1,F)
        self.q = np.array(qq)
        self.C = np.array(cc)
        return self.q,self.C
#    def __init__(self,Sample,Column,Interaction, Pump, time_factor=1 ):
#        super().__init__(Sample,Column,Interaction, Pump, time_factor=1 )
#        print(self.Sample.a)

        
        
if __name__=='__main__':
    
    n = 3
    a = time.time()
    sample = Sample(volume=0.1 , composition=np.ones(n)/n, concentration=1,
                    a=np.linspace(1,40,n), adsorption_max=np.linspace(0.025,0.04,n))
    
    sample.disp_concentration = [0 for _ in range(n)]
    sample.disp_concentration[-1] = 0.025
    pump = Pump(1)
    column = Column([1,20], 5*10**(-3), 0.635,pump, CFL=0.35)
    interaction = Interaction(sample)
    sim = Simu_with_D(sample,column,interaction,pump,time_factor=1)
    
    
    #%%
    sim.injection()
    
    #%%
    sim.simulation()

#    q = np.array(q)
#    C = np.array(C)
    b = time.time()
    Ausgabe = 'für {} Punkte braucht das Programm {} Sekunden'.format(np.product( sim.C.shape),(b-a))
    print(Ausgabe)