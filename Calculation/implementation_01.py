import numpy as np
import matplotlib.pyplot as plt
from column_01 import Column 
from pump_01 import Pump
from sample_01 import Sample
from interaction_01 import Interaction
from calculation_current import Simu
#from calculation_old_versions.calculation_13_fast import Simu
import time
import matplotlib.animation as animation
from itertools import cycle

plt.style.use('ggplot')

def prof():
    n = 6
    a = time.time()
    sample = Sample(volume=0.1 , composition=np.ones(n)/n, concentration=1,
                    a=np.linspace(1,40,n), adsorption_max=np.linspace(0.025,0.04,n))
    
    sample.disp_concentration = [0 for _ in range(n)]
    sample.disp_concentration[-1] = 0.025
    pump = Pump(1)
    column = Column([1,20], 5*10**(-3), 0.635,pump, CFL=0.35)
    interaction = Interaction(sample)
    sim = Simu(sample,column,interaction,pump,time_factor=1)
    
    #%%
    sim.injection()
    
    #%%
    sim.simulation()

#    q = np.array(q)
#    C = np.array(C)
    b = time.time()
    Ausgabe = 'für {} Punkte braucht das Programm {} Sekunden'.format(np.product( sim.C.shape),(b-a))
    print(Ausgabe)
    return sim,column
    
sim,column = prof()
#%% Plots
Writer = animation.writers['ffmpeg']
writer = Writer(fps=2, metadata=dict(artist='Me'), bitrate=1800)

col = np.linspace(1,column.geometry[1],int(column.geometry[1]//column.dz))

fig2 = plt.figure()  
lst = [i for i in range(0,sim.num_time_steps,20)]
gen = cycle(lst)

def funk(i):
    n = next(gen)
    plt.clf()
    for i in sim.num_components:
        plt.plot(col, sim.C[n,:,i]+sim.q[n,:,i], label='Komponente {}'.format(i))
    plt.grid(True, color='k', linestyle='--', linewidth='0.4')
    plt.legend()
    

im_ani = animation.FuncAnimation(fig2, funk, interval=500)
#%%
#im_ani.save('im1.mp4', writer=writer)

    



