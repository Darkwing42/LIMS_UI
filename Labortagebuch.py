# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Labortagebuch.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1075, 484)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(30, 30, 1021, 381))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnProbeAnlegen = QtWidgets.QPushButton(self.widget)
        self.btnProbeAnlegen.setObjectName("btnProbeAnlegen")
        self.horizontalLayout.addWidget(self.btnProbeAnlegen)
        self.btnAktualisieren = QtWidgets.QPushButton(self.widget)
        self.btnAktualisieren.setObjectName("btnAktualisieren")
        self.horizontalLayout.addWidget(self.btnAktualisieren)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnProbeAnlegen.setText(_translate("Form", "Probe anlegen"))
        self.btnAktualisieren.setText(_translate("Form", "Aktualisieren"))

