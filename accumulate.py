# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accumulate(object):
    def setupUi(self, Accumulate):
        Accumulate.setObjectName("Accumulate")
        Accumulate.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Accumulate)
        self.centralwidget.setObjectName("centralwidget")
        self.btnExam = QtWidgets.QPushButton(self.centralwidget)
        self.btnExam.setGeometry(QtCore.QRect(40, 50, 121, 61))
        self.btnExam.setObjectName("btnExam")
        self.btnAppend = QtWidgets.QPushButton(self.centralwidget)
        self.btnAppend.setGeometry(QtCore.QRect(190, 50, 121, 61))
        self.btnAppend.setObjectName("btnAppend")
        self.btnReview = QtWidgets.QPushButton(self.centralwidget)
        self.btnReview.setGeometry(QtCore.QRect(330, 50, 121, 61))
        self.btnReview.setObjectName("btnReview")
        Accumulate.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accumulate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Accumulate.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Accumulate)
        self.statusbar.setObjectName("statusbar")
        Accumulate.setStatusBar(self.statusbar)

        self.retranslateUi(Accumulate)
        QtCore.QMetaObject.connectSlotsByName(Accumulate)

    def retranslateUi(self, Accumulate):
        _translate = QtCore.QCoreApplication.translate
        Accumulate.setWindowTitle(_translate("Accumulate", "MainWindow"))
        self.btnExam.setText(_translate("Accumulate", "Examination"))
        self.btnAppend.setText(_translate("Accumulate", "Append"))
        self.btnReview.setText(_translate("Accumulate", "Review"))

