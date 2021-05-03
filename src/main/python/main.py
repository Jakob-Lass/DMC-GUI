#from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
try:
    from DMC_GUI import DMCMainWindow,updateSplash
    from Views.splash_screen import Ui_SplashScreen
except ImportError:
    import os
    os.chdir(os.path.dirname(__file__))
    from DMC_GUI.src.main.python.DMC_GUI import DMCMainWindow,updateSplash
    from DMC_GUI.src.main.python.Views.splash_screen import Ui_SplashScreen
    
from PyQt5 import QtWidgets, QtGui, QtCore
import datetime


from fbs_runtime.application_context.PyQt5 import ApplicationContext, \
    cached_property
    
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self,'<strong>DMC<\strong>Gui')

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.counter = 0.0
        self.ui.setProgress(self.counter)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        # ## ==> APPLY DROP SHADOW EFFECT
        # self.shadow = QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(20)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QColor(0, 0, 0, 120))
        # self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        #self.timer.start(3)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        
    def setProgress(self,counter,description):


        if counter>100:
            counter = 100
        self.ui.setProgress(counter,description=description)
        QtWidgets.QApplication.processEvents()


class AppContext(ApplicationContext):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.splash_screen = SplashScreen()
        self.splash_screen.show()

        
        QtWidgets.QApplication.processEvents()

        

    def run(self):
        
        QtWidgets.QApplication.processEvents()
        
        if len(sys.argv)==2:
            self.main_window.loadGui(presetFileLocation=sys.argv[1])

        self.main_window.show()
        self.splash_screen.close()
        return self.app.exec_()

    @cached_property
    def main_window(self):
        QtWidgets.QApplication.processEvents()
        res = DMCMainWindow(self,splash_screen = self.splash_screen)

        return res # Pass context to the window.


def main():
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)

if __name__ == '__main__':
    import os
    os.environ["QT_LOGGING_RULES"] = "*.debug=false"
    main()
