# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hauptfenster.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1280, 800)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 1241, 731))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnLabortagebuch = QtGui.QPushButton(self.widget)
        self.btnLabortagebuch.setObjectName(_fromUtf8("btnLabortagebuch"))
        self.horizontalLayout.addWidget(self.btnLabortagebuch)
        self.btnErgebnisse = QtGui.QPushButton(self.widget)
        self.btnErgebnisse.setObjectName(_fromUtf8("btnErgebnisse"))
        self.horizontalLayout.addWidget(self.btnErgebnisse)
        self.btnErgebnisse_2 = QtGui.QPushButton(self.widget)
        self.btnErgebnisse_2.setObjectName(_fromUtf8("btnErgebnisse_2"))
        self.horizontalLayout.addWidget(self.btnErgebnisse_2)
        self.btnStammdaten = QtGui.QPushButton(self.widget)
        self.btnStammdaten.setObjectName(_fromUtf8("btnStammdaten"))
        self.horizontalLayout.addWidget(self.btnStammdaten)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtGui.QListWidget(self.widget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.btnAktualisierenProben = QtGui.QPushButton(self.widget)
        self.btnAktualisierenProben.setObjectName(_fromUtf8("btnAktualisierenProben"))
        self.verticalLayout.addWidget(self.btnAktualisierenProben)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.listWidget_3 = QtGui.QListWidget(self.widget)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.horizontalLayout_2.addWidget(self.listWidget_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.calendarWidget = QtGui.QCalendarWidget(self.widget)
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.verticalLayout_2.addWidget(self.calendarWidget)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setEnabled(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget_2 = QtGui.QListWidget(self.widget)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.btnNeuerTermin = QtGui.QPushButton(self.widget)
        self.btnNeuerTermin.setObjectName(_fromUtf8("btnNeuerTermin"))
        self.verticalLayout_2.addWidget(self.btnNeuerTermin)
        self.btnAktualisierenTermine = QtGui.QPushButton(self.widget)
        self.btnAktualisierenTermine.setObjectName(_fromUtf8("btnAktualisierenTermine"))
        self.verticalLayout_2.addWidget(self.btnAktualisierenTermine)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionDebug = QtGui.QAction(MainWindow)
        self.actionDebug.setObjectName(_fromUtf8("actionDebug"))
        self.menuFile.addAction(self.actionEdit)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionDebug)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnLabortagebuch.setText(_translate("MainWindow", "Labortagebuch", None))
        self.btnErgebnisse.setText(_translate("MainWindow", "Ergebnisse", None))
        self.btnErgebnisse_2.setText(_translate("MainWindow", "Ergebnisse", None))
        self.btnStammdaten.setText(_translate("MainWindow", "Stammdaten", None))
        self.label.setText(_translate("MainWindow", "Proben heute:", None))
        self.btnAktualisierenProben.setText(_translate("MainWindow", "Aktualisieren", None))
        self.label_2.setText(_translate("MainWindow", "Termine", None))
        self.btnNeuerTermin.setText(_translate("MainWindow", "Neuer Termin", None))
        self.btnAktualisierenTermine.setText(_translate("MainWindow", "Aktualisieren", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionEdit.setText(_translate("MainWindow", "Edit", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionDebug.setText(_translate("MainWindow", "Debug", None))

