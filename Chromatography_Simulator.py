from PyQt5.QtWidgets import QApplication
from Graphs.fig_01 import PlotCanvas
from Graphs.graphChromaCanvas import PlotCanvas_Chrom 
from Graphs.Popup_ai import popup
from fa_02 import App
import sys
import numpy as np


class main(App):
    
    def __init__(self):
        super().__init__()
        self.ui.resetButton.clicked.connect(self.reset_Data)  
        self.m = PlotCanvas(self.ui.graphColumn_2, width=7, height=4.5, dpi=100)
        self.mm = PlotCanvas_Chrom(self.ui.graphChromatogram, width=7, height=4.5)
        self.ui.horizontalScrollBar.valueChanged.connect(self.changeGraphColumn)
        self.ui.adsoptionIsotherm.clicked.connect(self.show_AI)    
        self.show()
        self.rezise_graph()
    
    def rezise_graph(self):
        geom = self.ui.graphChromatogram.geometry()
        self.mm.resize(geom.width(),geom.height())
        self.m.resize(geom.width(),geom.height())
    
    def show_AI(self):
        self.get_settings()
        self.ui_graph = popup(self.sample)

    def changeChromatogram(self):
        geom = self.ui.graphChromatogram.geometry()
        self.mm.resize(geom.width(),geom.height())
        showAll = self.ui.showAllC.checkState()
        n = self.ui.horizontalScrollBar.value()
        if n >= self.C.shape[0]-1:
            n = self.C.shape[0]-1
        concentration = self.ui.doubleSpin_Concentration_Column.value()
        x_axes = np.linspace(0,n*self.column.dt, n)
        dz = self.C.shape[0]*self.column.dt
        self.mm.plot(range(len(self.C[0,0,:])),x_axes,self.C,self.q,n, concentration, dz,showAll)
       
    def changeGraphColumn(self):
        geom = self.ui.graphColumn_2.geometry()
        self.m.resize(geom.width(),geom.height())
        n = self.ui.horizontalScrollBar.value()
        if n >= self.C.shape[0]-1:
            n = self.C.shape[0]-1
        concentration = self.ui.doubleSpin_Concentration_Column.value()
        col = np.linspace(1,self.column.geometry[1]-1,int(self.column.geometry[1]//self.column.dz)-1)
        self.m.plot(range(len(self.C[0,0,:])),col,self.C,self.q,n,concentration)
        self.changeChromatogram()

    def reset_Data(self):
        self.C = None
        self.q = None
        if self.simu != None:
            self.simu.C = None
            self.simu.q = None
        else: pass
        
if __name__ =='__main__':
    
    app = QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)

    ex = main()
    sys.exit(app.exec_())