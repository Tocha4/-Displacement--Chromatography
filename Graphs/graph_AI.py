# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_AI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Graph_AI(object):
    def setupUi(self, Graph_AI):
        Graph_AI.setObjectName("Graph_AI")
        Graph_AI.resize(732, 514)
        Graph_AI.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Graph_AI.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout = QtWidgets.QGridLayout(Graph_AI)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_AI = QtWidgets.QGraphicsView(Graph_AI)
        self.graphicsView_AI.setObjectName("graphicsView_AI")
        self.gridLayout.addWidget(self.graphicsView_AI, 0, 0, 1, 1)

        self.retranslateUi(Graph_AI)
        QtCore.QMetaObject.connectSlotsByName(Graph_AI)

    def retranslateUi(self, Graph_AI):
        _translate = QtCore.QCoreApplication.translate
        Graph_AI.setWindowTitle(_translate("Graph_AI", "Frame"))

