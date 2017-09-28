from PyQt5.QtWidgets import QApplication
import sys
import numpy as np
import matplotlib.pyplot as plt
import os

if 'Ui_Graph_AI' in os.listdir():
    from graph_AI import Ui_Graph_AI
    from graphAiCanvas import PlotCanvas_AI
else:
    from Graphs.graph_AI import Ui_Graph_AI
    from Graphs.graphAiCanvas import PlotCanvas_AI
    
from PyQt5.QtWidgets import QFrame


class popup(QFrame):
    
    def __init__(self, Sample):
        super().__init__()
        self.ui_graph = Ui_Graph_AI()
        self.ui_graph.setupUi(self)   
        self.ai = PlotCanvas_AI(self.ui_graph.graphicsView_AI, width=7, height=4.5)
        self.ai.create_AI(Sample)
        self.show()
        geom = self.ui_graph.graphicsView_AI.geometry()
        self.ai.resize(geom.width(),geom.height())
 

    

if __name__ =='__main__':
    
    app = QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)

    ex = popup()
    sys.exit(app.exec_())