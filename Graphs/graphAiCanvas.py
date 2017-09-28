from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

 
class PlotCanvas_AI(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = None
        
    def create_AI(self, Sample):
        x = np.linspace(0,1,100)
        q_max = np.array(Sample.max_adsorption)
        a = np.array(Sample.a)
        f = lambda i: q_max*a*i/(1+a*i)
        y = np.array([f(i) for i in x])
        Line = plt.Line2D([0,max(Sample.disp_concentration)],[0,f(max(Sample.disp_concentration))[-1]],linewidth=2, color='black')
        for i in range(len(y[0,:])):
            self.axes.plot(x,y[:,i], label='component {}'.format(i))
        self.axes.add_line(Line)
        self.axes.set_xlabel('C [g/ml]', size=12)
        self.axes.set_ylabel('q [g/ml]', size=12)
        self.axes.grid(True, color='k', linestyle='--', linewidth='0.4')
        self.axes.set_title('Adsorption Isotherm')
        self.axes.legend()
 
if __name__=='__main__':
    
    m = PlotCanvas()
    ax = m.figure.add_subplot(111)
    