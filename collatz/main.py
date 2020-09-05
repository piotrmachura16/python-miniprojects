"""This is the `__main__` module."""
import sys
import os
from PyQt5 import QtWidgets, QtGui
from app import CollatzApp

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dir_name = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QtGui.QIcon(dir_name + os.path.sep + 'icon.svg'))
    ex = CollatzApp()
    app.exec()
