import numpy as np
class Displacer(object):
    def __init__(self, disp_concentration=0):
        self.disp_concentration = disp_concentration

class Sample(Displacer):
    '''
    volume: cm**3 or ml
    composition: composition of the sample [part_1, part_2,...] g/ml or g/cm**3
    concentration: concentration of the composition in the sample 0 < concentration < 1
    
    INHERITANCE
    disp_concentration: concentration of the displacer [disp, part_2 = 0,...]
    
    '''

    def __init__(self, volume, composition, concentration, a,adsorption_max):
        self.volume = volume
        self.composition = composition
        self.concentration = concentration
        self.a = np.array(a)
        self.max_adsorption = adsorption_max


if __name__ == '__main__':
    
#    a = Displacer(7)
    sample1 = Sample(1,2,3)
    sample1.disp_concentration = 5
    print(sample1.disp_concentration)