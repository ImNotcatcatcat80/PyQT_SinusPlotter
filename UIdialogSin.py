# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sinuses_UIdialog.ui'
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

class Ui_MainWindowDialog(object):
    def setupUi(self, MainWindowDialog):
        MainWindowDialog.setObjectName(_fromUtf8("MainWindowDialog"))
        MainWindowDialog.resize(518, 353)
        self.centralwidget = QtGui.QWidget(MainWindowDialog)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButtonInDialog = QtGui.QPushButton(self.centralwidget)
        self.pushButtonInDialog.setGeometry(QtCore.QRect(150, 70, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonInDialog.setFont(font)
        self.pushButtonInDialog.setObjectName(_fromUtf8("pushButtonInDialog"))
        self.lcdNumberClicks = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumberClicks.setGeometry(QtCore.QRect(190, 190, 141, 51))
        self.lcdNumberClicks.setObjectName(_fromUtf8("lcdNumberClicks"))
        self.labelThisW = QtGui.QLabel(self.centralwidget)
        self.labelThisW.setGeometry(QtCore.QRect(10, 20, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelThisW.setFont(font)
        self.labelThisW.setObjectName(_fromUtf8("labelThisW"))
        MainWindowDialog.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowDialog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowDialog.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowDialog)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowDialog.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindowDialog)

    def retranslateUi(self, MainWindowDialog):
        MainWindowDialog.setWindowTitle(_translate("MainWindowDialog", "Dialog Window", None))
        self.pushButtonInDialog.setText(_translate("MainWindowDialog", "H", None))
        self.labelThisW.setText(_translate("MainWindowDialog", "labelThisW", None))

