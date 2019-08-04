# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examination.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd
import random


class Ui_Examination(object):

    data = pd.read_csv("F:/accumulate.csv", encoding='gbk')
    quantity = 20 if 20 < data.shape[0] else data.shape[0]
    rand_list = random.sample(range(data.shape[0]), quantity)
    index = 0
    word = tuple(data.iloc[rand_list[index], :])

    def setupUi(self, Examination):
        Examination.setObjectName("Examination")
        Examination.resize(382, 273)
        self.label = QtWidgets.QLabel(Examination)
        self.label.setGeometry(QtCore.QRect(20, 20, 331, 21))
        self.label.setObjectName("label")
        self.ChnTxt = QtWidgets.QLineEdit(Examination)
        self.ChnTxt.setGeometry(QtCore.QRect(20, 40, 281, 21))
        self.ChnTxt.setObjectName("ChnTxt")
        self.label_2 = QtWidgets.QLabel(Examination)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 281, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Examination)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 281, 21))
        self.lineEdit.setObjectName("lineEdit")
 #       self.label.grabKeyboard()
        self.btnSubmit = QtWidgets.QPushButton(Examination)
        self.btnSubmit.setGeometry(QtCore.QRect(130, 150, 93, 28))
        self.btnSubmit.setObjectName("btnSubmit")
        self.pushButton = QtWidgets.QPushButton(Examination)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.btnNext = QtWidgets.QPushButton(Examination)
        self.btnNext.setGeometry(QtCore.QRect(240, 150, 93, 28))
        self.btnNext.setObjectName("btnNext")

        self.retranslateUi(Examination)
        QtCore.QMetaObject.connectSlotsByName(Examination)

    def retranslateUi(self, Examination):
        _translate = QtCore.QCoreApplication.translate
        Examination.setWindowTitle(_translate("Examination", "Dialog"))
        self.label.setText(_translate("Examination", "Please input the spell of this word:"))
        self.label_2.setText(_translate("Examination", "Spelling:"))
        self.btnSubmit.setText(_translate("Examination", "Submit"))
        self.pushButton.setText(_translate("Examination", "Delete"))
        self.btnNext.setText(_translate("Examination", "Next"))

    def setupfunc(self):
        self.btnSubmit.clicked.connect(self.judge)
        self.pushButton.clicked.connect(self.delete)
        self.btnNext.clicked.connect(self.Next)
        self.ChnTxt.setText(self.word[1])
        self.lineEdit.setText("")

    def judge(self):
        Eng = self.lineEdit.text()
        if(Eng == self.word[0]):
            self.lineEdit.setText("Congratulations, U R right!")
        else:
            self.lineEdit.setText("Sorry,it's " + self.word[0])

    def Next(self):
        self.lineEdit.setText("")
        self.index = self.index + 1
        if self.index < self.quantity:
            self.word = tuple(self.data.iloc[self.rand_list[self.index], :])
            self.ChnTxt.setText(self.word[1])

    def delete(self):
        pass

