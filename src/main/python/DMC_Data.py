from PyQt5 import QtCore
from DMCpy import DataSet,DataFile
import numpy as np
#from collections import defaultdict

class GuiDataSet(DataSet.DataSet):
    def __init__(self,dataFiles=None,name='No Name', **kwargs):
        super(GuiDataSet,self).__init__(dataFiles=dataFiles,**kwargs)
        self.name = name
        #self.currentNormalizationSettings = defaultdict(lambda: None) # Holder for newest settings
        #self.normalizationSettings = defaultdict(lambda: None) # Holder for latest used settings
        
    
    def setData(self,column,value):
        if column == 0: self.name = value
    

    def flags(self):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable


                
class GuiDataFile(DataFile.DataFile):
    def __init__(self,fileLocation, **kwargs):
        super(GuiDataFile,self).__init__(filePath=fileLocation,**kwargs)
        self.name = self.fileName
        self.type = 'hdf'

    def setData(self,column,value):
        if column == 0: self.name = value

    def flags(self):
        return QtCore.Qt.ItemIsEditable


