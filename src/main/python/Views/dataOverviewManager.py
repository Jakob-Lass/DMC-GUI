import sys
sys.path.append('..')

import matplotlib.pyplot as plt


try:
    from DMCGui.src.main.python._tools import ProgressBarDecoratorArguments
    import DMCGui.src.main.python._tools as _GUItools
    from DMCGui.src.main.python.GuiStates import States
except ImportError:
    from _tools import ProgressBarDecoratorArguments
    from GuiStates import States,highlightStyle,normalStyle
    import _tools as _GUItools
from os import path
from PyQt5 import QtWidgets,uic
import numpy as np

# Handles all functionality related to the View3D box. Each button has its own 
# definition, which should be pretty selfexplanatory.

# def View3D_setCAxis_button_function(self):
#     if not hasattr(self, 'V'):
#         self.View3D_plot_button_function()
        
#     CAxisMin=float(self.ui.View3D_CAxisMin_lineEdit.text())
#     CAxisMax=float(self.ui.View3D_CAxisMax_lineEdit.text())
            
#     self.V.set_clim(CAxisMin,CAxisMax)


try:
    dataOverviewManagerBase, dataOverviewManagerForm = uic.loadUiType(path.join(path.dirname(__file__),"dataOverview.ui"))
except:
    try:
        dataOverviewManagerBase, dataOverviewManagerForm = uic.loadUiType(path.join(path.dirname(__file__),'..','..','resources','base','Views',"dataOverview.ui"))
    except:
        dataOverviewManagerBase, dataOverviewManagerForm = uic.loadUiType(path.join(path.dirname(__file__),'..','resources','base','Views',"dataOverview.ui"))
# All of this connects the buttons and their functions to the main window.

class dataOverviewManager(dataOverviewManagerBase, dataOverviewManagerForm):
    def __init__(self, parent=None, guiWindow=None):
        super(dataOverviewManager, self).__init__(parent)
        self.setupUi(self)
        self.guiWindow = guiWindow
        self.guiWindow.dataOverviewManager = self
        self.initdataOverviewManager()
        
    def initdataOverviewManager(self):    
        self.guiWindow.dataOverviewManager_setCAxis_button_function = lambda:plotOverview(self.guiWindow)
        self.guiWindow.dataOverviewManager_updateGrid_function = lambda value=None:updateGrid(self.guiWindow,value)
        self.guiWindow.dataOverviewManager_updateTitlefunction = lambda title=None:updateTitle(self.guiWindow,title)
        self.guiWindow.dataOverviewManager_updateCLim_function = lambda cmin=None,cmax=None:updateCLim(self.guiWindow,cmin,cmax)
        self.guiWindow.dataOverviewManager_updateColorbar_function = lambda value=None:updateColorbar(self.guiWindow,value)
        #self.guiWindow.dataOverviewManager_extractInputs = lambda:extractInputs(self.guiWindow)


        for key,value in self.__dict__.items():
            if 'DataOverview' in key:
                self.guiWindow.ui.__dict__[key] = value

    def setup(self):
        self.guiWindow.ui.DataOverview_plot_button.clicked.connect(self.guiWindow.dataOverviewManager_setCAxis_button_function)
        self.guiWindow.state_changed.connect(self.guiStateChanged)

        self.guiWindow.ui.DataOverview_CAxisMin_spinBox.valueChanged.connect(self.guiWindow.dataOverviewManager_updateCLim_function)
        self.guiWindow.ui.DataOverview_CAxisMax_spinBox.valueChanged.connect(self.guiWindow.dataOverviewManager_updateCLim_function)

        self.guiWindow.ui.DataOverview_Colorbar_checkBox.stateChanged.connect(self.guiWindow.dataOverviewManager_updateColorbar_function)

        self.guiWindow.ui.DataOverview_Grid_checkBox.stateChanged.connect(self.guiWindow.dataOverviewManager_updateGrid_function)

        

    def guiStateChanged(self,newState):
        if not newState == States.FULL:
           self.guiWindow.ui.DataOverview_plot_button.setEnabled(False)
           self.guiWindow.ui.DataOverview_plot_button.setStyleSheet(normalStyle)
           return

        self.guiWindow.ui.DataOverview_plot_button.setEnabled(True)
        self.guiWindow.ui.DataOverview_plot_button.setStyleSheet(highlightStyle)

    def extractInputs(self):
        """Extract input parameters for plotting function
        
        Returns:
        
            - dict containing extracted values

        """
        
        setupDict = {'thetaStart':self.guiWindow.ui.DataOverview_TwoThetaBinningStart_spinBox.value(),
                      'thetaStep': self.guiWindow.ui.DataOverview_TwoThetaBinningStep_spinBox.value(),
                      'thetaStop': self.guiWindow.ui.DataOverview_TwoThetaBinningStop_spinBox.value(),
  
                      'vmin': self.guiWindow.ui.DataOverview_CAxisMin_spinBox.value(),
                      'vmax': self.guiWindow.ui.DataOverview_CAxisMax_spinBox.value(),
                      'colorbar': self.guiWindow.ui.DataOverview_Colorbar_checkBox.isChecked(),
  
                      'grid': self.guiWindow.ui.DataOverview_Grid_checkBox.isChecked(),
                      'FMT': self.guiWindow.ui.DataOverview_fmt_lineEdit.text(),
                      'title': self.guiWindow.ui.DataOverview_SetTitle_lineEdit.text()
                    }
        return setupDict

@ProgressBarDecoratorArguments(runningText='Generating Overview Plot',completedText='Overview Plot Generated')  
def plotOverview(self):

    # Get input parameters
    setupDict = self.dataOverviewManager.extractInputs()

    thetaBins = np.arange(setupDict['thetaStart']-0.5*setupDict['thetaStep'],
                            setupDict['thetaStop'] +0.5*setupDict['thetaStep'],
                            setupDict['thetaStep'])

    ds = self.DataSetModel.getCurrentDataSet()
    
    kwargs = {'twoThetaBins':thetaBins}
                            #'fmt':setupDict['FMT'],'colorbar':setupDict['colorbar']}

    title = setupDict['title']
    grid = setupDict['grid']
    vmin,vmax = [setupDict[xx] for xx in ['vmin','vmax']]
    colorbar = setupDict['colorbar']
    
    
    AX = ds.plotOverview(**kwargs)
    self.plotOverviewAxes = AX

    self.dataOverviewManager_updateGrid_function(grid)
    self.dataOverviewManager_updateTitlefunction(title=title)
    self.dataOverviewManager_updateCLim_function(vmin,vmax)
    self.dataOverviewManager_updateColorbar_function(colorbar)

    self.windows.append(AX[0].get_figure())
    
    return True

def updateGrid(self,value=None):
    if hasattr(self,'plotOverviewAxes'): # Check if a plotOverview has been created
        AX = self.plotOverviewAxes

        if value is None:
            value = self.guiWindow.ui.DataOverview_Grid_checkBox.isChecked()
        
        for ax in AX:
            ax.grid(value)

def updateCLim(self,cmin=None,cmax=None):
    if hasattr(self,'plotOverviewAxes'): # Check if a plotOverview has been created
        AX = self.plotOverviewAxes

        if hasattr(AX[0],'set_clim'):
            if cmin is None:
                cmin = self.guiWindow.ui.DataOverview_CAxisMin_spinBox.value()
            if cmax is None:
                cmax = self.guiWindow.ui.DataOverview_CAxisMax_spinBox.value()

            AX[0].set_clim(cmin,cmax)
    


def updateTitle(self,title=None):
    if hasattr(self,'plotOverviewAxes'): # Check if a plotOverview has been created
        AX = self.plotOverviewAxes

        if title is None:
            title = self.guiWindow.ui.DataOverview_SetTitle_lineEdit.text()
        
        fig = AX[0].get_figure()
        fig.suptitle(title)

        fig.tight_layout()

def updateColorbar(self,value=None):
    
    if hasattr(self,'plotOverviewAxes'): # Check if a plotOverview has been created
        AX = self.plotOverviewAxes
        if hasattr(AX[0],'_imshow'): # It contains data for which a colorbar makes sense
            if value is None:
                value = self.guiWindow.ui.DataOverview_Colorbar_checkBox.isChecked()
            
            if hasattr(AX[0],'_colorbar'): # colorbar already exists
                if value: # Set the colorbar (from previously removed)
                    AX[0]._colorbar.ax.set_visible(True)
                    # Reset AX[0] to original size
                    AX[0].set_position(AX[0]._originalPos)
                else:
                    AX[0]._colorbar.ax.set_visible(False)
                    # Set position as before but copyu width from AX[1]
                    bbox = AX[0].get_position()
                    pos = [*bbox.p0,AX[1].get_position().width,bbox.height]
                    AX[0].set_position(pos)
                    
            elif value: # No colorbar but want one
                    AX[0]._colorbar = AX[0].get_figure().colorbar(AX[0]._imshow,ax=AX[0])
                    AX[0]._originalPos = AX[0].get_position()