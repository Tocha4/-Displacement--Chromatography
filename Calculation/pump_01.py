

class Pump(object):
    '''
    volume_flow_min: velocity of the volume ml/min
    volume_flow_sec: velocity of the volume ml/sec
    '''
    def __init__(self, volume_flow_min):
        self.volume_flow_min = volume_flow_min
        self.volume_flow_sec = self.volume_flow_min/60
        