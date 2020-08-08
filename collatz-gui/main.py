import sys
import os
from app import CollatzApp
from PyQt5 import QtWidgets, QtGui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon.svg'))
    ex = CollatzApp()
    app.exec()
