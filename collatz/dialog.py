"""This module contains the custom dialog box."""
import os
from PyQt5 import QtGui, QtWidgets, QtCore


class BrowserDialog(QtWidgets.QDialog):
    """ This is a custom dialog box for opening the Collatz
    conjecture Wikipedia page in a web browser.
    """

    def __init__(self, *args, **kwargs):
        super(BrowserDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Info")
        self.setWindowIcon(QtGui.QIcon(
            os.path.dirname(__file__) + '/icon.svg'))

        # Buttons
        q_btn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.button_box = QtWidgets.QDialogButtonBox(q_btn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.message = QtWidgets.QLabel(
            'This will open your browser.\nContinue?', self)
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)
