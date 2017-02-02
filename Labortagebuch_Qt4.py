# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Labortagebuch.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1075, 484)
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(30, 30, 1021, 381))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.treeWidget = QtGui.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnProbeAnlegen = QtGui.QPushButton(self.widget)
        self.btnProbeAnlegen.setObjectName(_fromUtf8("btnProbeAnlegen"))
        self.horizontalLayout.addWidget(self.btnProbeAnlegen)
        self.btnAktualisieren = QtGui.QPushButton(self.widget)
        self.btnAktualisieren.setObjectName(_fromUtf8("btnAktualisieren"))
        self.horizontalLayout.addWidget(self.btnAktualisieren)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnProbeAnlegen.setText(_translate("Form", "Probe anlegen", None))
        self.btnAktualisieren.setText(_translate("Form", "Aktualisieren", None))

