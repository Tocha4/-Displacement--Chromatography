from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

 
class PlotCanvas_Chrom(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def new_plot(self,num_components,x_axes,C,q,n,concentration, dz, showAll):
        bx = self.figure.add_subplot(111)
        if showAll == 0:
            bx.plot(x_axes, C[:n,-2,:].sum(axis=1)+q[:n,-2,:].sum(axis=1))
        else:
            for i in num_components:        
                bx.plot(x_axes, C[:n,-2,i]+q[:n,-2,i]) #, label='Komponente {}'.format(i)
        bx.set_xlim([0,dz]) 
        bx.set_ylim([0,concentration])
        bx.set_xlabel('Time [sec]', size=7)
        bx.set_ylabel('Concentration [g/ml]')
        bx.grid(True, color='k', linestyle='--', linewidth='0.4')
        bx.legend()
        
        return bx
        
 
    def plot(self,num_components,x_axes,C,q,n, concentration, dz, showAll):        
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax = self.new_plot(num_components,x_axes,C,q,n, concentration, dz, showAll)
        self.ax.set_title('Chromatogram')
        self.draw()
        
 
if __name__=='__main__':
    
    m = PlotCanvas()
    ax = m.figure.add_subplot(111)
    