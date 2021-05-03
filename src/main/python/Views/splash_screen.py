# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenLzRFkI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import QWidget,QFrame,QGridLayout,QLabel

import time


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen,applicationName=r'<strong>Your<\strong> Application',progressValue=0.0):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.container)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 251, 231))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.percentage_lineEdit = QLabel(self.layoutWidget)
        self.percentage_lineEdit.setObjectName(u"percentage_lineEdit")
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(36)
        self.percentage_lineEdit.setFont(font)
        self.percentage_lineEdit.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.percentage_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.percentage_lineEdit, 1, 0, 1, 1)

        self.labelLoadingInfo = QLabel(self.layoutWidget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(9)
        self.labelLoadingInfo.setFont(font1)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)

        self.title_lineEdit = QLabel(self.layoutWidget)
        self.title_lineEdit.setObjectName(u"title_lineEdit")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(22)
        self.title_lineEdit.setFont(font2)
        self.title_lineEdit.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.title_lineEdit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title_lineEdit, 0, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        #self.retranslateUi(SplashScreen)
        self.setApplicationName(applicationName)
        self.setProgress(progressValue)

        QMetaObject.connectSlotsByName(SplashScreen)


    def setApplicationName(self,name):
            self.title_lineEdit.setText(QCoreApplication.translate("SplashScreen", name, None))

    def setProgress(self,value,description=None,percentageFMT=u"{:.1f}%"): # value between 0 and 100, description shows text in "loading..." field
        #print(value,description)
        if value<0:
                value = 0.0
        elif value>100.0:
                value = 100.0
        
        if description is None:
                description = 'loading...'
        
        self.percentage_lineEdit.setText(QCoreApplication.translate("SplashScreen", percentageFMT.format(value), None))
        self.labelLoadingInfo.setText(QCoreApplication.translate("SplashScreen", description, None))

        # Translate to value between 1 and 0:
        progress = (100.0 - value) / 100.0 
        
        gradientRegion = 0.05

        p1 = progress-gradientRegion
        if p1<0:
                p1 = 0.0
        
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:"""+"{:2f}".format(p1)+" rgba(255, 0, 127, 0), stop:{:2f}".format(progress)+\
                        """ rgba(85, 170, 255, 255));
        }
        """
        self.circularProgress.setStyleSheet(styleSheet)

        time.sleep(0.15)

