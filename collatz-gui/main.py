import sys
from app import CollatzApp
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CollatzApp()
    sys.exit(app.exec_())
