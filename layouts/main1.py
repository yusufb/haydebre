# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from main import _translate
from functions import *

class anaMenu1(object):
    def setupUi(self, MainWindow):

        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 692)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget.setStyleSheet("background:url(kocayusuf.png)")

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 180, 251, 71))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet("background:#CCC")
        self.pushButton_2.clicked.connect(functions.changeLayout)
        self.pushButton_2.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), lambda: functions.changeLayout("layout degistirildi"))

        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 260, 251, 71))
        self.pushButton_3.setStyleSheet("background:#CCC")
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 340, 251, 71))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("background:#CCC")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pencere 1", None))
        self.pushButton_2.setText(_translate("MainWindow", "Yeni Oyun", None))
        self.pushButton_3.setText(_translate("MainWindow", "Sezona Devam Et", None))
        self.pushButton_4.setText(_translate("MainWindow", "Hakkımızda", None))

    def printHeyy(self):
        print "heyy"
        




