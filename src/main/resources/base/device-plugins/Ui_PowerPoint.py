# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Code\Mcntrl\src\main\resources\base\device-plugins\PowerPoint.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 213)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filebox = QtWidgets.QLineEdit(self.centralwidget)
        self.filebox.setGeometry(QtCore.QRect(10, 61, 231, 21))
        self.filebox.setObjectName("filebox")
        self.loadfile = QtWidgets.QPushButton(self.centralwidget)
        self.loadfile.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.loadfile.setObjectName("loadfile")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 301, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.prevslide = QtWidgets.QPushButton(self.centralwidget)
        self.prevslide.setGeometry(QtCore.QRect(10, 130, 161, 23))
        self.prevslide.setObjectName("prevslide")
        self.nextslide = QtWidgets.QPushButton(self.centralwidget)
        self.nextslide.setGeometry(QtCore.QRect(164, 130, 151, 23))
        self.nextslide.setObjectName("nextslide")
        self.gotoslide = QtWidgets.QPushButton(self.centralwidget)
        self.gotoslide.setGeometry(QtCore.QRect(210, 160, 101, 31))
        self.gotoslide.setObjectName("gotoslide")
        self.slidenum = QtWidgets.QLineEdit(self.centralwidget)
        self.slidenum.setGeometry(QtCore.QRect(10, 160, 201, 31))
        self.slidenum.setObjectName("slidenum")
        self.startslideshow = QtWidgets.QPushButton(self.centralwidget)
        self.startslideshow.setGeometry(QtCore.QRect(10, 90, 301, 23))
        self.startslideshow.setObjectName("startslideshow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filebox.setText(_translate("MainWindow", "Enter File Name"))
        self.loadfile.setText(_translate("MainWindow", "Load File"))
        self.label.setText(_translate("MainWindow", "Files go into the install media folder"))
        self.label_2.setText(_translate("MainWindow", "Power Point Controller"))
        self.prevslide.setText(_translate("MainWindow", "Previous Slide"))
        self.nextslide.setText(_translate("MainWindow", "Next Slide"))
        self.gotoslide.setText(_translate("MainWindow", "Go To Slide"))
        self.startslideshow.setText(_translate("MainWindow", "Start Slideshow"))
