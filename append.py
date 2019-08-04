# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'append.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd

class Ui_Append(object):
    def setupUi(self, Append):
        Append.setObjectName("Append")
        Append.resize(372, 163)
        self.label = QtWidgets.QLabel(Append)
        self.label.setGeometry(QtCore.QRect(80, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Append)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Append)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Append)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btnApd = QtWidgets.QPushButton(Append)
        self.btnApd.setGeometry(QtCore.QRect(180, 100, 121, 41))
        self.btnApd.setObjectName("btnApd")

        self.retranslateUi(Append)
        QtCore.QMetaObject.connectSlotsByName(Append)

    def retranslateUi(self, Append):
        _translate = QtCore.QCoreApplication.translate
        Append.setWindowTitle(_translate("Append", "Dialog"))
        self.label.setText(_translate("Append", "English"))
        self.label_2.setText(_translate("Append", "Chinese"))
        self.btnApd.setText(_translate("Append", "APPEND"))

    def setupfunction(self):
        self.btnApd.clicked.connect(self.upload)

    def upload(self):
        Eng = self.lineEdit.text()
        Chn = self.lineEdit_2.text()
        csvfile = open("F:/accumulate.csv", "a", newline='')
        writer = csv.writer(csvfile)
        writer.writerow([Eng, Chn])
        csvfile.close()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")


