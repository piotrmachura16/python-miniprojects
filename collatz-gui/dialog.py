import os
from PyQt5 import QtGui, QtWidgets, QtCore


class BrowserDialog(QtWidgets.QDialog):
    """ This is a custom dialog box for opening the Collatz conjecture Wikipedia page in a web browser.
    """

    def __init__(self, *args, **kwargs):
        super(BrowserDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Info")
        self.setWindowIcon(QtGui.QIcon(
            os.path.dirname(__file__) + '/icon.svg'))

        # Buttons
        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.message = QtWidgets.QLabel(
            'This will open your browser.\nContinue?', self)
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
