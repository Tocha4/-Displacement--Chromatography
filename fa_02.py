import sys 
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from DC_01 import Ui_DC_MainWindow
from Calculation.sample_01 import Sample
from Calculation.column_01 import Column 
from Calculation.pump_01 import Pump
from Calculation.interaction_01 import Interaction
from Calculation.calculation_current import Simu
#from Calculation.calculation_old_versions.calculation_13_fast import Simu
import time
import numpy as np
#from fig_01 import PlotCanvas
#from graphChromaCanvas import PlotCanvas_Chrom


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DC_MainWindow()
        self.ui.setupUi(self)
        self.ui.Einlesen.clicked.connect(self.get_item)
        self.ui.acceptSettings.clicked.connect(self.get_settings)
        self.ui.loadSettings.clicked.connect(self.openFileNameDialog)
        self.ui.StartSimulation.clicked.connect(self.start_simulation)
        self.ui.SaveSettingsButton.clicked.connect(self.saveFileNameDialog)
        self.ui.saveDataButton.clicked.connect(self.save_Data)
        self.ui.loadDataBotton.clicked.connect(self.load_Data)
#        self.show()
        self.sample = None
        self.pump = None
        self.column = None
        self.interaction = None
        self.simu = None
        
    
        
    def get_item(self): 
        item = self.ui.spinBox.value()
        self.ui.Settings.setColumnCount(item)
        
    def openFileNameDialog(self):
        types = "All Files (*);;Text Files (*.txt)"
        filename, answare = QFileDialog.getOpenFileNames(self, 'Load Sample Settings', 
                                                         '',
                                                         types,'two')  
        if answare != 'two':
            with open(filename[0]) as f:
                data = [[float(j) for j in i[:-1].split(',')] for i in f]
            self.set_settings(data)

    def saveFileNameDialog(self):
        types = "All Files (*);;Text Files (*.txt)"
        filename, answare = QFileDialog.getSaveFileName(self, 'Save Sample Settings', 
                                                         '',
                                                         types,'two')   
        if answare != 'two':
            print(filename, answare)
            self.save_settings(filename)
        
    def set_settings(self, data):
        self.ui.SampleConcentrationSpinBox.setValue(data[4][0])
        self.ui.SampleVolumeSpinBox.setValue(data[5][0])   
        self.ui.Settings.setColumnCount(len(data[0]))
        rows = range(len(data[0]))
        columns = range(4)
        for i in columns:
            for j in rows:
                item = QTableWidgetItem(str(data[i][j]))
                self.ui.Settings.setItem(i,j,item)         
        for n,i in enumerate(data[6:]):
            item = QTableWidgetItem(str(i[0]))
            self.ui.TSettingsTable.setItem(n,0,item)
    
    def get_settings(self):
        self.time_factor = self.ui.timeFactor.value()
        rows = range(self.ui.Settings.columnCount())
        columns = range(self.ui.Settings.rowCount())
        sample_settings = [[],[],[],[]]
        for i in columns:
            for j in rows:
                item = self.ui.Settings.item(i,j)
                sample_settings[i].append(float(item.text()))
        self.sample = Sample(volume=self.ui.SampleVolumeSpinBox.value(),  
                             composition=sample_settings[0], 
                             concentration=self.ui.SampleConcentrationSpinBox.value()/100, 
                             a=sample_settings[2],
                             adsorption_max=sample_settings[3])
        self.sample.disp_concentration = sample_settings[1]
        vf = self.ui.TSettingsTable.item(0,0)
        self.pump = Pump(float(vf.text()))
        geometry = [self.ui.TSettingsTable.item(1,0),self.ui.TSettingsTable.item(2,0)]
        particle_size = self.ui.TSettingsTable.item(3,0)
        porosity = self.ui.TSettingsTable.item(4,0)
        geometry = [float(i.text()) for i in geometry]
        self.CFL = self.ui.CFL_spinbox.value()
        self.column = Column(geometry, float(particle_size.text()), float(porosity.text()), self.pump, n_columns=1, CFL=self.CFL)
        if 'Settings' not in os.listdir():
            print('Settings' in os.listdir())
            os.mkdir(os.path.join(os.getcwd(),'Settings'))
        self.save_settings(os.path.join(os.getcwd(),'Settings/last_settings.txt'))
                
    def start_simulation(self):
        a = time.time()
        self.interaction = Interaction(self.sample)
        self.simu = Simu(self.sample,self.column,self.interaction,self.pump, time_factor=self.time_factor)
        self.simu.injection()
        self.q,self.C = self.simu.simulation()
        self.simu.enable()
        b = time.time()
        Ausgabe = 'For {} points the program takes {} seconds.'.format(np.product([i for i in self.C.shape]),(b-a))
        print(Ausgabe)
        self.ui.horizontalScrollBar.setMaximum(self.C.shape[0])
        
    def save_settings(self,path):
        self.data_settings = [self.sample.composition,self.sample.disp_concentration,
                 list(self.sample.a), self.sample.max_adsorption,
                 self.sample.concentration*100, self.sample.volume, 
                 self.pump.volume_flow_min, self.column.geometry[0],
                 self.column.geometry[1], self.column.particle_size,
                 self.column.porosity]
        with open(path, 'w') as ls:
            for i in self.data_settings:
                ls.write(str(i).strip('[]')+'\n')
        
    def save_Data(self):
        types = "All Files (*);;Text Files (*.npy)"
        filename, answare = QFileDialog.getSaveFileName(self, 'Save Data', 
                                                         '',
                                                         types,'two')   
        
        if answare != 'two':
            
            np.save('{}.npy'.format(filename), (self.q,self.C))
            with open('{}.txt'.format(filename), 'w') as ls:
                for i in self.data_settings:
                    ls.write(str(i).strip('[]')+'\n')
           
    def load_Data(self):
        types = "All Files (*);;Text Files (*.npy)"
        filename, answare = QFileDialog.getOpenFileName(self, 'Load Data', 
                                                         '',
                                                         types,'two')  
        if answare != 'two':
            self.q, self.C = np.load(filename)
            with open('{}.txt'.format(filename[:-4])) as f:
                data = [[float(j) for j in i[:-1].split(',')] for i in f]
            self.set_settings(data)
            self.ui.horizontalScrollBar.setMaximum(self.C.shape[0])
            self.get_settings()



if __name__=='__main__':
    
    app = QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)

    ex = App()
    sys.exit(app.exec_())
