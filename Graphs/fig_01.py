from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

 
class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=15, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax = None
        
    def new_plot(self,num_components,col,C,q,n,concentration):
        bx = self.figure.add_subplot(111)
        for i in num_components:
            bx.plot(col, C[n,:-1,i]+q[n,:-1,i], label='Komponente {}'.format(i))
            
        bx.set_ylim([0,concentration])
        bx.grid(True, color='k', linestyle='--', linewidth='0.4')
        bx.set_xlabel('Column length [cm]',size=7)
        bx.set_ylabel('Amount in the column [g/ml]')
        bx.legend()
        return bx
        
 
    def plot(self,num_components,col,C,q,n,concentration):        
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax = self.new_plot(num_components,col,C,q,n,concentration)
        self.ax.set_title('Inside the column')
        self.draw()
 
if __name__=='__main__':
    
    m = PlotCanvas()
    ax = m.figure.add_subplot(111)
    