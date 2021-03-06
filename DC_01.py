# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DC_01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DC_MainWindow(object):
    def setupUi(self, DC_MainWindow):
        DC_MainWindow.setObjectName("DC_MainWindow")
        DC_MainWindow.resize(1194, 1042)
        DC_MainWindow.setToolTipDuration(0)
        self.centralwidget = QtWidgets.QWidget(DC_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMaximumSize(QtCore.QSize(14777195, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphColumn_2 = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphColumn_2.setObjectName("graphColumn_2")
        self.gridLayout_2.addWidget(self.graphColumn_2, 0, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.widget_7)
        self.horizontalScrollBar.setSingleStep(5)
        self.horizontalScrollBar.setSliderPosition(0)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.widget_6 = QtWidgets.QWidget(self.widget_7)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.doubleSpin_Concentration_Column = QtWidgets.QDoubleSpinBox(self.widget_6)
        self.doubleSpin_Concentration_Column.setDecimals(3)
        self.doubleSpin_Concentration_Column.setMaximum(1.0)
        self.doubleSpin_Concentration_Column.setSingleStep(0.1)
        self.doubleSpin_Concentration_Column.setProperty("value", 0.04)
        self.doubleSpin_Concentration_Column.setObjectName("doubleSpin_Concentration_Column")
        self.horizontalLayout_6.addWidget(self.doubleSpin_Concentration_Column)
        self.showAllC = QtWidgets.QCheckBox(self.widget_6)
        self.showAllC.setObjectName("showAllC")
        self.horizontalLayout_6.addWidget(self.showAllC)
        self.verticalLayout.addWidget(self.widget_6)
        self.gridLayout_2.addWidget(self.widget_7, 1, 0, 1, 1)
        self.graphChromatogram = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphChromatogram.setObjectName("graphChromatogram")
        self.gridLayout_2.addWidget(self.graphChromatogram, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setEnabled(True)
        self.widget_9.setObjectName("widget_9")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_9)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget_9)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 430))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMaximum(20)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.Einlesen = QtWidgets.QPushButton(self.widget)
        self.Einlesen.setObjectName("Einlesen")
        self.horizontalLayout.addWidget(self.Einlesen)
        self.loadSettings = QtWidgets.QPushButton(self.widget)
        self.loadSettings.setObjectName("loadSettings")
        self.horizontalLayout.addWidget(self.loadSettings)
        self.verticalLayout_5.addWidget(self.widget)
        self.Settings = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setMaximumSize(QtCore.QSize(12777215, 16777215))
        self.Settings.setRowCount(4)
        self.Settings.setColumnCount(3)
        self.Settings.setObjectName("Settings")
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.Settings.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Settings.setItem(3, 2, item)
        self.Settings.horizontalHeader().setDefaultSectionSize(50)
        self.Settings.horizontalHeader().setMinimumSectionSize(20)
        self.verticalLayout_5.addWidget(self.Settings)
        self.adsoptionIsotherm = QtWidgets.QPushButton(self.groupBox)
        self.adsoptionIsotherm.setObjectName("adsoptionIsotherm")
        self.verticalLayout_5.addWidget(self.adsoptionIsotherm)
        self.widget_3 = QtWidgets.QWidget(self.groupBox)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.SampleVolumeSpinBox = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.SampleVolumeSpinBox.setDecimals(3)
        self.SampleVolumeSpinBox.setProperty("value", 1.0)
        self.SampleVolumeSpinBox.setObjectName("SampleVolumeSpinBox")
        self.horizontalLayout_3.addWidget(self.SampleVolumeSpinBox)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.groupBox)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.SampleConcentrationSpinBox = QtWidgets.QSpinBox(self.widget_4)
        self.SampleConcentrationSpinBox.setMaximum(100)
        self.SampleConcentrationSpinBox.setProperty("value", 100)
        self.SampleConcentrationSpinBox.setObjectName("SampleConcentrationSpinBox")
        self.horizontalLayout_4.addWidget(self.SampleConcentrationSpinBox)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_9)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName("formLayout")
        self.TSettingsTable = QtWidgets.QTableWidget(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TSettingsTable.sizePolicy().hasHeightForWidth())
        self.TSettingsTable.setSizePolicy(sizePolicy)
        self.TSettingsTable.setBaseSize(QtCore.QSize(0, 0))
        self.TSettingsTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TSettingsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.TSettingsTable.setIconSize(QtCore.QSize(0, 0))
        self.TSettingsTable.setRowCount(5)
        self.TSettingsTable.setColumnCount(2)
        self.TSettingsTable.setObjectName("TSettingsTable")
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TSettingsTable.setItem(4, 1, item)
        self.TSettingsTable.horizontalHeader().setDefaultSectionSize(50)
        self.TSettingsTable.verticalHeader().setCascadingSectionResizes(False)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TSettingsTable)
        self.widget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_8 = QtWidgets.QWidget(self.widget_5)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget_8)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.CFL_spinbox = QtWidgets.QDoubleSpinBox(self.widget_8)
        self.CFL_spinbox.setDecimals(3)
        self.CFL_spinbox.setMinimum(0.01)
        self.CFL_spinbox.setMaximum(5.0)
        self.CFL_spinbox.setSingleStep(0.05)
        self.CFL_spinbox.setProperty("value", 0.35)
        self.CFL_spinbox.setObjectName("CFL_spinbox")
        self.verticalLayout_2.addWidget(self.CFL_spinbox)
        self.label_3 = QtWidgets.QLabel(self.widget_8)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setLineWidth(1)
        self.label_3.setScaledContents(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.timeFactor = QtWidgets.QDoubleSpinBox(self.widget_8)
        self.timeFactor.setDecimals(1)
        self.timeFactor.setMinimum(1.0)
        self.timeFactor.setMaximum(10.0)
        self.timeFactor.setSingleStep(0.5)
        self.timeFactor.setProperty("value", 2.0)
        self.timeFactor.setObjectName("timeFactor")
        self.verticalLayout_2.addWidget(self.timeFactor)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.SaveSettingsButton = QtWidgets.QPushButton(self.widget_5)
        self.SaveSettingsButton.setObjectName("SaveSettingsButton")
        self.verticalLayout_3.addWidget(self.SaveSettingsButton)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widget_5)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.groupBox_4)
        self.acceptSettings = QtWidgets.QPushButton(self.widget_9)
        self.acceptSettings.setObjectName("acceptSettings")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.acceptSettings)
        self.widget_2 = QtWidgets.QWidget(self.widget_9)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.StartSimulation = QtWidgets.QPushButton(self.widget_2)
        self.StartSimulation.setObjectName("StartSimulation")
        self.horizontalLayout_2.addWidget(self.StartSimulation)
        self.saveDataButton = QtWidgets.QPushButton(self.widget_2)
        self.saveDataButton.setObjectName("saveDataButton")
        self.horizontalLayout_2.addWidget(self.saveDataButton)
        self.loadDataBotton = QtWidgets.QPushButton(self.widget_2)
        self.loadDataBotton.setObjectName("loadDataBotton")
        self.horizontalLayout_2.addWidget(self.loadDataBotton)
        self.resetButton = QtWidgets.QPushButton(self.widget_2)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.widget_2)
        self.widget_2.raise_()
        self.groupBox.raise_()
        self.groupBox_4.raise_()
        self.acceptSettings.raise_()
        self.gridLayout_3.addWidget(self.widget_9, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        DC_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DC_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1194, 19))
        self.menubar.setObjectName("menubar")
        DC_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DC_MainWindow)
        self.statusbar.setObjectName("statusbar")
        DC_MainWindow.setStatusBar(self.statusbar)
        self.actionAsdfasd = QtWidgets.QAction(DC_MainWindow)
        self.actionAsdfasd.setObjectName("actionAsdfasd")
        self.actionAdjfa_ldkfj = QtWidgets.QAction(DC_MainWindow)
        self.actionAdjfa_ldkfj.setObjectName("actionAdjfa_ldkfj")

        self.retranslateUi(DC_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(DC_MainWindow)

    def retranslateUi(self, DC_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        DC_MainWindow.setWindowTitle(_translate("DC_MainWindow", "Displacement Chromatography Simulator"))
        self.groupBox_3.setTitle(_translate("DC_MainWindow", "Simulation"))
        self.showAllC.setText(_translate("DC_MainWindow", "Show all components"))
        self.groupBox.setTitle(_translate("DC_MainWindow", "Adsorption Settings"))
        self.spinBox.setToolTip(_translate("DC_MainWindow", "<html><head/><body><p>How many Components are in the Sample?</p></body></html>"))
        self.Einlesen.setText(_translate("DC_MainWindow", "Accept Number of Components"))
        self.loadSettings.setText(_translate("DC_MainWindow", "Load Settings"))
        item = self.Settings.verticalHeaderItem(0)
        item.setText(_translate("DC_MainWindow", "Composition"))
        item = self.Settings.verticalHeaderItem(1)
        item.setText(_translate("DC_MainWindow", "Disp_Composition"))
        item = self.Settings.verticalHeaderItem(2)
        item.setText(_translate("DC_MainWindow", "a_const"))
        item = self.Settings.verticalHeaderItem(3)
        item.setText(_translate("DC_MainWindow", "q_max"))
        __sortingEnabled = self.Settings.isSortingEnabled()
        self.Settings.setSortingEnabled(False)
        item = self.Settings.item(0, 0)
        item.setText(_translate("DC_MainWindow", "0.3"))
        item = self.Settings.item(0, 1)
        item.setText(_translate("DC_MainWindow", "0.3"))
        item = self.Settings.item(0, 2)
        item.setText(_translate("DC_MainWindow", "0.3"))
        item = self.Settings.item(1, 0)
        item.setText(_translate("DC_MainWindow", "0"))
        item = self.Settings.item(1, 1)
        item.setText(_translate("DC_MainWindow", "0"))
        item = self.Settings.item(1, 2)
        item.setText(_translate("DC_MainWindow", "0.05"))
        item = self.Settings.item(2, 0)
        item.setText(_translate("DC_MainWindow", "1"))
        item = self.Settings.item(2, 1)
        item.setText(_translate("DC_MainWindow", "5"))
        item = self.Settings.item(2, 2)
        item.setText(_translate("DC_MainWindow", "15"))
        item = self.Settings.item(3, 0)
        item.setText(_translate("DC_MainWindow", "0.01"))
        item = self.Settings.item(3, 1)
        item.setText(_translate("DC_MainWindow", "0.025"))
        item = self.Settings.item(3, 2)
        item.setText(_translate("DC_MainWindow", "0.04"))
        self.Settings.setSortingEnabled(__sortingEnabled)
        self.adsoptionIsotherm.setText(_translate("DC_MainWindow", "Show adsoption isotherm"))
        self.label.setText(_translate("DC_MainWindow", "Sample volume [ml]: "))
        self.label_2.setText(_translate("DC_MainWindow", "Sample concentration [%]: "))
        self.groupBox_4.setTitle(_translate("DC_MainWindow", "Technical settings"))
        item = self.TSettingsTable.verticalHeaderItem(0)
        item.setText(_translate("DC_MainWindow", "Volume Flow"))
        item = self.TSettingsTable.verticalHeaderItem(1)
        item.setText(_translate("DC_MainWindow", "Column Diameter"))
        item = self.TSettingsTable.verticalHeaderItem(2)
        item.setText(_translate("DC_MainWindow", "Column Length"))
        item = self.TSettingsTable.verticalHeaderItem(3)
        item.setText(_translate("DC_MainWindow", "Particle Diameter"))
        item = self.TSettingsTable.verticalHeaderItem(4)
        item.setText(_translate("DC_MainWindow", "Porosity"))
        __sortingEnabled = self.TSettingsTable.isSortingEnabled()
        self.TSettingsTable.setSortingEnabled(False)
        item = self.TSettingsTable.item(0, 0)
        item.setText(_translate("DC_MainWindow", "1"))
        item = self.TSettingsTable.item(0, 1)
        item.setText(_translate("DC_MainWindow", "ml/min"))
        item = self.TSettingsTable.item(1, 0)
        item.setText(_translate("DC_MainWindow", "1"))
        item = self.TSettingsTable.item(1, 1)
        item.setText(_translate("DC_MainWindow", "cm"))
        item = self.TSettingsTable.item(2, 0)
        item.setText(_translate("DC_MainWindow", "20"))
        item = self.TSettingsTable.item(2, 1)
        item.setText(_translate("DC_MainWindow", "cm"))
        item = self.TSettingsTable.item(3, 0)
        item.setText(_translate("DC_MainWindow", "0.005"))
        item = self.TSettingsTable.item(3, 1)
        item.setText(_translate("DC_MainWindow", "cm"))
        item = self.TSettingsTable.item(4, 0)
        item.setText(_translate("DC_MainWindow", "0.635"))
        item = self.TSettingsTable.item(4, 1)
        item.setText(_translate("DC_MainWindow", "-"))
        self.TSettingsTable.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("DC_MainWindow", "CFL"))
        self.label_3.setText(_translate("DC_MainWindow", "Time factor: "))
        self.SaveSettingsButton.setText(_translate("DC_MainWindow", "Save Settings"))
        self.acceptSettings.setToolTip(_translate("DC_MainWindow", "<html><head/><body><p>Accept the data in the table.</p></body></html>"))
        self.acceptSettings.setText(_translate("DC_MainWindow", "Accept Settings"))
        self.StartSimulation.setText(_translate("DC_MainWindow", "Start Simulation"))
        self.saveDataButton.setText(_translate("DC_MainWindow", "Save Data"))
        self.loadDataBotton.setText(_translate("DC_MainWindow", "Load Data"))
        self.resetButton.setText(_translate("DC_MainWindow", "RESET DATA"))
        self.actionAsdfasd.setText(_translate("DC_MainWindow", "asdfasd"))
        self.actionAdjfa_ldkfj.setText(_translate("DC_MainWindow", "adjfaöldkfj"))

