#from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
try:
    from DMC_GUI import DMCMainWindow,updateSplash
except ImportError:
    import os
    os.chdir(os.path.dirname(__file__))
    from DMC_GUI.src.main.python.DMC_GUI import DMCMainWindow,updateSplash
    
from PyQt5 import QtWidgets, QtGui, QtCore
import datetime


from fbs_runtime.application_context.PyQt5 import ApplicationContext, \
    cached_property
    

class AppContext(ApplicationContext):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap(self.get_resource('splash.png')))                                    
        
        self.splash.show()
        
        self.timer = QtCore.QTimer() 
        
        updateInterval = 400 # ms
        originalTime = datetime.datetime.now()
        
        updater = lambda:updateSplash(self.splash,originalTime=originalTime,updateInterval=updateInterval)
        updater()
        
        
        self.timer.timeout.connect(updater) 
        self.timer.setInterval(updateInterval)
        self.timer.start()
        QtWidgets.QApplication.processEvents()

        

    def run(self):
        
        QtWidgets.QApplication.processEvents()
        self.splash.finish(self.main_window)
        self.main_window.show()

        if len(sys.argv)==2:
            self.main_window.loadGui(presetFileLocation=sys.argv[1])
        return self.app.exec_()

    @cached_property
    def main_window(self):
        QtWidgets.QApplication.processEvents()
        res = DMCMainWindow(self)
        self.timer.stop()
        return res # Pass context to the window.


def main():
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)

if __name__ == '__main__':
    import os
    os.environ["QT_LOGGING_RULES"] = "*.debug=false"
    main()
