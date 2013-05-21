# -*- coding: utf-8 -*-
from layouts import *
from functions import *
from PyQt4 import QtCore, QtGui

#UTF-8 support for the game
def _translate(context, text, disambig):
    try:
        _encoding = QtGui.QApplication.UnicodeUTF8
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
    except AttributeError:
        return QtGui.QApplication.translate(context, text, disambig)
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except Error:
    def _fromUtf8(s):
        return s

class layout:
    @staticmethod
    def drawLayout(layoutClass):
        return layoutClass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    className = layout.drawLayout(anaMenu1)
    ui = className()

    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())