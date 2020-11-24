#global imports
import sys, os
import win32com, win32com.client
from pathlib import Path
from PyQt5 import uic, QtWidgets
import Ui_PowerPoint

#Power Point Controller
class PowerPointUi(QtWidgets.QMainWindow):
    def __init__(self, a_id=1):
        """Create new powerpoint control interface"""
        super(PowerPointUi, self).__init__()
        self.id = a_id
        raw_path = Path(os.getcwd()).parent
        self.pptdir = raw_path.__str__() + "/media/"
        print("Loading: "+str(self.pptdir))

        #establish gui
        self.uippt = Ui_PowerPoint.Ui_MainWindow()
        self.uippt.setupUi(self)
    
    def connect_com32(self):
        """Connect to Power Point Instance"""
        self.a = win32com.client.Dispatch("PowerPoint.Application")
        print("Successfully connected to Powerpoint ID: "+str(self.id))

    def ppt_open(self, filename):
        """Open Power Point"""
        print("Opening pptx: " + str(self.pptdir + filename))
        self.pptcntrl = self.a.Presentations.Open(FileName=self.pptdir + filename, WithWindow=1)

    def ppt_ss(self):
        """Start Slideshow"""
        self.pptcntrl.SlideShowSettings.run()

    def ppt_es(self):
        """Exist Slideshow"""
        self.pptcntrl.SlideShowWindow.View.Exit()

    def ppt_ns(self):
        """Next Slide"""
        self.pptcntrl.SlideShowWindow.View.Next()

    def ppt_ps(self):
        """Previous/Last Displayed Slide"""
        self.pptcntrl.SlideShowWindow.View.Previous()

    def ppt_gs(self, slide_index):
        """Goto Slide at slide_index"""
        self.pptcntrl.SlideShowWindow.View.GoToSlide(slide_index)

    def ppt_close(self):
        """Close powerpoint slideshow"""
        self.pptcntrl.Close()

    def ppt_quit(self):
        """Quit Powerpoint (NOT FUNCTIONAL)"""
        self.a.Quit()

    def create_slots(self):
        #slots
        self.uippt.loadfile.clicked.connect(lambda: self.ppt_open(str(self.uippt.filebox.text())))
        self.uippt.prevslide.clicked.connect(lambda: self.ppt_ps())
        self.uippt.nextslide.clicked.connect(lambda: self.ppt_ns())
        self.uippt.gotoslide.clicked.connect(lambda: self.ppt_gs(str(self.uippt.slidenum.text())))
        self.uippt.startslideshow.clicked.connect(lambda: self.ppt_ss())

    def closeEvent(self, event):
        print("Shutting down Power Point Handler")
        self.ppt_close()
        self.ppt_quit()

    def createGUI(self, instance):
        """Create Control GUI"""
        app = QtWidgets.QApplication(sys.argv)
        window = instance
        window.create_slots()
        window.show()
        app.exec_()