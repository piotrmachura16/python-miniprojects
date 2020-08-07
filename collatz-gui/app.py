import sys
import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from IntValidator import IntValidator
from StepsDisplay import StepsDisplay
from BrowserDialog import BrowserDialog


class CollatzApp(QtWidgets.QMainWindow):
    '''
    This is a Qt5 GUI for checking your favourite natural numbers against the Collatz conjecture.
    '''

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
        '''
        Initialize the app UI. Only gets called once at the end of the constructor.
        '''
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(
            os.path.dirname(__file__) + '/icon.svg'))

        # Create start button
        self.startButton = QtWidgets.QPushButton('Start', self)
        self.startButton.clicked.connect(self.on_click_start)

        # Create textbox for number input
        self.inputbox = QtWidgets.QLineEdit(self)
        self.inputbox.setValidator(IntValidator(bottom=1))
        self.inputbox.resize(self.width - 40, 50)
        # Enter to press 'Start' button
        self.inputbox.returnPressed.connect(self.startButton.click)
        # Set textbox font
        self.inputbox.font()
        f = self.inputbox.font()
        f.setPointSize(14)
        self.inputbox.setFont(f)

        # Create textarea for iterations display
        self.steps = StepsDisplay(self)

        # Create clear button
        self.clearButton = QtWidgets.QPushButton('Clear', self)
        self.clearButton.clicked.connect(self.on_click_clear)

        # Create info button
        self.infoButton = QtWidgets.QPushButton('Info', self)
        self.infoButton.clicked.connect(self.on_click_info)

        # Add widgets to window
        hbox_top = QtWidgets.QHBoxLayout()
        hbox_top.addWidget(self.inputbox)
        hbox_top.addWidget(self.startButton)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(hbox_top)
        vbox.addWidget(self.steps)
        hbox_bottom = QtWidgets.QHBoxLayout()
        hbox_bottom.addStretch()
        hbox_bottom.addWidget(self.clearButton)
        hbox_bottom.addWidget(self.infoButton)
        vbox.addLayout(hbox_bottom)
        # Central widget
        central = QtWidgets.QWidget(self)
        central.setLayout(vbox)
        self.setCentralWidget(central)
        self.show()

    def check(self, n):
        '''
        Perform a recursive check with the Collatz sequence as described here: https://en.wikipedia.org/wiki/Collatz_conjecture .

        Raises an exception and terminates when the sequence reaches 1.
        '''
        self.steps.insertPlainText(str(n))
        if n == 1:
            self.steps.insertPlainText('\n')
            raise Exception()
        else:
            self.counter += 1
            if n % 2 == 0:
                self.steps.insertPlainText('\t| /2\n')
                self.check(int(n / 2))
            else:
                self.steps.insertPlainText('\t| *3 + 1\n')
                self.check(int(3 * n + 1))

    @ QtCore.pyqtSlot()
    def on_click_start(self):
        '''
        Starts the Collatz sequence calculations.
        '''
        self.steps.clear()
        try:
            textboxValue = int(self.inputbox.text())
        except Exception:
            # Empty input - ignore
            return
        try:
            self.counter = 0
            self.check(textboxValue)
        except Exception:
            self.steps.insertPlainText(
                f'Terminated after {self.counter} iterations.')
            self.steps.moveCursor(QtGui.QTextCursor.End)

    @ QtCore.pyqtSlot()
    def on_click_clear(self):
        '''
        Clears the input box and steps display.
        '''
        self.inputbox.clear()
        self.steps.clear()
        self.inputbox.setFocus()

    @ QtCore.pyqtSlot()
    def on_click_info(self):
        '''
        Opens a dialog window and the Collatz conjecture Wikipedia article if the user chooses so.
        '''
        if BrowserDialog(self).exec_():
            webbrowser.open('https://en.wikipedia.org/wiki/Collatz_conjecture')
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CollatzApp()
    sys.exit(app.exec_())
