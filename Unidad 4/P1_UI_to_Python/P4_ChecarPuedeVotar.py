# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P4_ChecarPuedeVotar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#pyuic5 P4_ChecarPuedeVotar.ui -o P4_ChecarPuedeVotar.py


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 171, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../3D Objects/UAT.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 0, 161, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../3D Objects/facultad_ingenieria_tampico.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 300, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../3D Objects/Castor.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 0, 141, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/Logos/UAT.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 290, 131, 81))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/Logos/Castor Ingeniero.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 10, 161, 61))
        self.label_8.setStyleSheet("background-image: url(:/NLogos/Facultad.jpg);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Logos/Facultad.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.Bcomprobar = QtWidgets.QPushButton(self.centralwidget)
        self.Bcomprobar.setGeometry(QtCore.QRect(320, 250, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bcomprobar.setFont(font)
        self.Bcomprobar.setObjectName("Bcomprobar")
        self.Tedad = QtWidgets.QLineEdit(self.centralwidget)
        self.Tedad.setGeometry(QtCore.QRect(280, 141, 161, 31))
        self.Tedad.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.Tedad.setObjectName("Tedad")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bcomprobar.setText(_translate("MainWindow", "Comprobar"))
        self.label.setText(_translate("MainWindow", "Edad"))
import Recursos_rc
