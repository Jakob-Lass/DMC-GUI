# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 340))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 798, 851))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fixedOpen = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixedOpen.sizePolicy().hasHeightForWidth())
        self.fixedOpen.setSizePolicy(sizePolicy)
        self.fixedOpen.setMinimumSize(QtCore.QSize(200, 300))
        self.fixedOpen.setObjectName("fixedOpen")
        self.verticalLayout.addWidget(self.fixedOpen)
        self.collapsibleContainer = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.collapsibleContainer.setObjectName("collapsibleContainer")
        self.verticalLayout.addWidget(self.collapsibleContainer)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(6, 6, 6, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.progressBar_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_label.sizePolicy().hasHeightForWidth())
        self.progressBar_label.setSizePolicy(sizePolicy)
        self.progressBar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_label.setObjectName("progressBar_label")
        self.verticalLayout_3.addWidget(self.progressBar_label)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        #self.menuMask = QtWidgets.QMenu(self.menubar)
        #self.menuMask.setObjectName("menuMask")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        #self.menuTools = QtWidgets.QMenu(self.menubar)
        #self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_GUI_state = QtWidgets.QAction(MainWindow)
        self.actionSave_GUI_state.setObjectName("actionSave_GUI_state")
        #self.actionSave_GUI_state.setShortcut("Ctrl+S")
        self.actionLoad_GUI_state = QtWidgets.QAction(MainWindow)
        self.actionLoad_GUI_state.setObjectName("actionLoad_GUI_state")
        self.actionLoad_GUI_state.setShortcut("Ctrl+L")
        #self.actionGenerate_View3d_script = QtWidgets.QAction(MainWindow)
        #self.actionGenerate_View3d_script.setObjectName("actionGenerate_View3d_script")
        #self.actionGenerate_QELine_script = QtWidgets.QAction(MainWindow)
        #self.actionGenerate_QELine_script.setObjectName("actionGenerate_QELine_script")
        #self.actionGenerate_QPlane_script = QtWidgets.QAction(MainWindow)
        #self.actionGenerate_QPlane_script.setObjectName("actionGenerate_QPlane_script")
        #self.actionGenerate_1d_script = QtWidgets.QAction(MainWindow)
        #self.actionGenerate_1d_script.setObjectName("actionGenerate_1d_script")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+Q")
        #self.actionOpen_mask_gui = QtWidgets.QAction(MainWindow)
        #self.actionOpen_mask_gui.setObjectName("actionOpen_mask_gui")
        #self.actionLoad_mask = QtWidgets.QAction(MainWindow)
        #self.actionLoad_mask.setObjectName("actionLoad_mask")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setShortcut("Ctrl+?")
        self.actionMolecularWeight = QtWidgets.QAction(MainWindow)
        self.actionMolecularWeight.setObjectName("actionMolecularWeight")
        self.actionNeutronCalculations = QtWidgets.QAction(MainWindow)
        self.actionNeutronCalculations.setObjectName("actionNeutronCalculations")
        self.actionNormalizationWidget = QtWidgets.QAction(MainWindow)
        self.actionNormalizationWidget.setObjectName("actionNormalizationWidget")
        self.actionPredictionWidget = QtWidgets.QAction(MainWindow)
        self.actionPredictionWidget.setObjectName("actionPredictionWidget")
        self.actionPredictionWidget.setShortcut("Ctrl+P")
        self.actionElectronicLogbook = QtWidgets.QAction("actionElectronicLogbook")
        self.actionElectronicLogbook.setObjectName("actionElectronicLogbook")
        self.actionChange_Theme = QtWidgets.QAction(MainWindow)
        self.actionChange_Theme.setObjectName("actionChange_Theme")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionClose_Windows = QtWidgets.QAction(MainWindow)
        self.actionClose_Windows.setObjectName("actionClose_Windows")
        self.menuFile.addAction(self.actionSave_GUI_state)
        self.menuFile.addAction(self.actionLoad_GUI_state)
        self.menuFile.addSeparator()
        #self.menuFile.addAction(self.actionGenerate_View3d_script)
        #self.menuFile.addAction(self.actionGenerate_QELine_script)
        #self.menuFile.addAction(self.actionGenerate_QPlane_script)
        #self.menuFile.addAction(self.actionGenerate_1d_script)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Windows)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        #self.menuMask.addAction(self.actionOpen_mask_gui)
        #self.menuMask.addAction(self.actionLoad_mask)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        #self.menuTools.addAction(self.actionPredictionWidget)
        #self.menuTools.addAction(self.actionMolecularWeight)
        #self.menuTools.addAction(self.actionNeutronCalculations)
        #self.menuTools.addAction(self.actionNormalizationWidget)
        #self.menuTools.addAction(self.actionElectronicLogbook)
        self.menubar.addAction(self.menuFile.menuAction())
        #self.menubar.addAction(self.menuMask.menuAction())
        #self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DMCGui"))
        self.progressBar_label.setText(_translate("MainWindow", "Ready"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        #self.menuMask.setTitle(_translate("MainWindow", "Mask"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        #self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionSave_GUI_state.setText(_translate("MainWindow", "Save GUI state"))
        self.actionLoad_GUI_state.setText(_translate("MainWindow", "Load GUI state"))
        #self.actionGenerate_View3d_.setText(_translate("MainWindow", "Generate View3D script"))
        #self.actionGenerate_QELine_script.setText(_translate("MainWindow", "Generate QELine script"))
        #self.actionGenerate_QPlane_script.setText(_translate("MainWindow", "Generate QPlane script"))
        #self.actionGenerate_1d_script.setText(_translate("MainWindow", "Generate 1D script"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        #self.actionOpen_mask_gui.setText(_translate("MainWindow", "Open Mask GUI"))
        #self.actionLoad_mask.setText(_translate("MainWindow", "Load Mask"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        #self.actionChange_Theme.setText(_translate("MainWindow", "Change Theme"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionClose_Windows.setText(_translate("MainWindow", "Close Windows"))
        #self.actionNormalizationWidget.setText(_translate("MainWindow","Generate Normalization"))
        #self.actionPredictionWidget.setText(_translate("MainWindow","Prediction Tool"))
        #self.actionMolecularWeight.setText(_translate("MainWindow","Calculate Molar Weight"))
        #self.actionNeutronCalculations.setText(_translate("MainWindow","Neutron Calculations"))
        #self.actionElectronicLogbook.setText(_translate("MainWindow","Electronic Logbook"))
