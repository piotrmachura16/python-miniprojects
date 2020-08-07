import sys
import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from validator import IntValidator
from display import ROTextArea
from dialog import BrowserDialog


class CollatzApp(QtWidgets.QMainWindow):
    """Main app window."""

    def __init__(self):
        super().__init__()
        self.title = ' Collatz'
        self.width = 550
        self.height = 700
        # Center the window
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.left = int(centerPoint.x()-self.width/2)
        self.top = int(centerPoint.y() - self.height / 2)
        self.initUI()

    def initUI(self):
        """Initialize the app UI. Only gets called once."""
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(
            os.path.dirname(__file__) + '/icon.svg'))

        # Create start button
        self.startButton = QtWidgets.QPushButton('Start', self)
        self.startButton.clicked.connect(self.on_click_start)

        # Create textbox for number input
        self.inputBox = QtWidgets.QLineEdit(self)
        self.inputBox.setValidator(IntValidator(bottom=1))
        self.inputBox.resize(self.width - 40, 50)
        # Enter to press 'Start' button
        self.inputBox.returnPressed.connect(self.startButton.click)
        # Set textbox font
        self.inputBox.font()
        f = self.inputBox.font()
        f.setPointSize(14)
        self.inputBox.setFont(f)

        # Create textarea for iterations display
        self.stepsDisplay = ROTextArea(self)

        # Create clear button
        self.clearButton = QtWidgets.QPushButton('Clear', self)
        self.clearButton.clicked.connect(self.on_click_clear)

        # Create info button
        self.infoButton = QtWidgets.QPushButton('Info', self)
        self.infoButton.clicked.connect(self.on_click_info)

        # Add widgets to window
        hBoxTop = QtWidgets.QHBoxLayout()
        hBoxTop.addWidget(self.inputBox)
        hBoxTop.addWidget(self.startButton)
        vBox = QtWidgets.QVBoxLayout()
        vBox.addLayout(hBoxTop)
        vBox.addWidget(self.stepsDisplay)
        hBoxBottom = QtWidgets.QHBoxLayout()
        hBoxBottom.addStretch()
        hBoxBottom.addWidget(self.clearButton)
        hBoxBottom.addWidget(self.infoButton)
        vBox.addLayout(hBoxBottom)
        # Central widget
        central = QtWidgets.QWidget(self)
        central.setLayout(vBox)
        self.setCentralWidget(central)
        self.show()
        self.inputBox.setFocus()

    def sequence(self, number):
        """Perform a recursive check with the Collatz sequence and print each step to `stepsDisplay`.

        Raises an `Exception` and terminates if the `number` is 1.
        """
        self.stepsDisplay.insertPlainText(str(number))
        if number == 1:
            self.stepsDisplay.insertPlainText('\n')
            raise Exception()
        else:
            self.counter += 1
            if number % 2 == 0:
                self.stepsDisplay.insertPlainText('\t| /2\n')
                self.sequence(int(number / 2))
            else:
                self.stepsDisplay.insertPlainText('\t| *3 + 1\n')
                self.sequence(int(3 * number + 1))

    @ QtCore.pyqtSlot()
    def on_click_start(self):
        """Clear the `stepsDisplay` and start the Collatz sequence."""
        self.stepsDisplay.clear()
        try:
            textboxValue = int(self.inputBox.text())
        except Exception:
            # Empty input - ignore
            return
        try:
            self.counter = 0
            self.sequence(textboxValue)
        except Exception:
            self.stepsDisplay.insertPlainText(
                f'Terminated after {self.counter} iterations.')
            self.stepsDisplay.moveCursor(QtGui.QTextCursor.End)

    @ QtCore.pyqtSlot()
    def on_click_clear(self):
        """Clear the `inputBox` and `stepsDisplay`."""
        self.inputBox.clear()
        self.stepsDisplay.clear()
        self.inputBox.setFocus()

    @ QtCore.pyqtSlot()
    def on_click_info(self):
        """Open a dialog window to acces the relevant Wikipedia article."""
        if BrowserDialog(self).exec_():
            webbrowser.open('https://en.wikipedia.org/wiki/Collatz_conjecture')
        else:
            pass
