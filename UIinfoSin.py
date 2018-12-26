# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sinuses_UIinfo.ui'
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

class Ui_DialogInfo(object):
    def setupUi(self, DialogInfo):
        DialogInfo.setObjectName(_fromUtf8("DialogInfo"))
        DialogInfo.resize(360, 120)
        self.labelInfoTitle = QtGui.QLabel(DialogInfo)
        self.labelInfoTitle.setGeometry(QtCore.QRect(10, 10, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelInfoTitle.setFont(font)
        self.labelInfoTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelInfoTitle.setObjectName(_fromUtf8("labelInfoTitle"))
        self.labelInfoText = QtGui.QLabel(DialogInfo)
        self.labelInfoText.setGeometry(QtCore.QRect(10, 30, 331, 21))
        self.labelInfoText.setObjectName(_fromUtf8("labelInfoText"))

        self.retranslateUi(DialogInfo)
        QtCore.QMetaObject.connectSlotsByName(DialogInfo)

    def retranslateUi(self, DialogInfo):
        DialogInfo.setWindowTitle(_translate("DialogInfo", "Dialog", None))
        self.labelInfoTitle.setText(_translate("DialogInfo", "Sinus Plotter", None))
        self.labelInfoText.setText(_translate("DialogInfo", "David Girardello, 2017 - 2018", None))

