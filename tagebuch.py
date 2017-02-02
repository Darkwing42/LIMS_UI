from PyQt4 import QtGui
import Labortagebuch_Qt4
import sys

class tagebuchApp(QtGui.QWidget, Labortagebuch_Qt4.Ui_Form):
    def __init__(self):
        super(tagebuchApp, self).__init__()
        self.setupUi(self)






