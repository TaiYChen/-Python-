# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'review.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 643)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 600, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 501, 541))
        self.textEdit.setObjectName("textEdit")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(500, 20, 20, 541))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def setupfunc(self):
        self.textEdit.clear()
        data = pd.read_csv("F:/accumulate.csv", encoding='gbk')
        wordlist = ""
        for i in range(data.shape[0]):
            Eng = data.iloc[i,0]
            Chn = data.iloc[i,1]
            Eng = Eng + "   " + Chn + "\r\n"
            wordlist = wordlist + Eng

        self.textEdit.setPlainText(wordlist)



