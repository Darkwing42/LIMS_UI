from PyQt4 import QtGui
import Hauptfenster_Qt4
import sys, os
import tagebuch

try:
    if sys.platform == 'win32':


class ExampleApp(QtGui.QMainWindow, Hauptfenster_Qt4.Ui_MainWindow):
    def __init__(self):
        super(ExampleApp, self).__init__()
        self.setupUi(self)
        self.btnLabortagebuch.clicked.connect(self.tagebuch)

    def tagebuch(self):
        #app = QtGui.QDialog(sys.argv)
        t = tagebuch.tagebuchApp()
        t.show()
        sys.exit(exec_())










def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()

    app.exec_()

if __name__ == '__main__':
    main()


