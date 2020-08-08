"""This module contains the main app window"""
import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from validator import IntValidator
from dialog import BrowserDialog


class CollatzApp(QtWidgets.QMainWindow):
    """Main app window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle(' Collatz')
        self.setFixedSize(550, 700)
        dir_name = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(dir_name + os.path.sep + 'icon.svg'))
        self.counter = 0

        # Create start button
        self.start_button = QtWidgets.QPushButton('Start', self)
        self.start_button.clicked.connect(self._on_click_start)

        # Create textbox for number input
        self.input_box = QtWidgets.QLineEdit(self)
        self.input_box.setValidator(IntValidator(bottom=1))
        # Enter to press 'Start' button
        self.input_box.returnPressed.connect(self.start_button.click)
        # Set textbox font
        self.input_box.font()
        font_ = self.input_box.font()
        font_.setPointSize(14)
        self.input_box.setFont(font_)

        # Create 'Steps' label
        self.steps_label = QtWidgets.QLabel(self)
        self.steps_label.setText('Steps')
        self.steps_label.setAlignment(QtCore.Qt.AlignCenter)
        font_ = self.steps_label.font()
        font_.setPointSize(10)
        self.steps_label.setFont(font_)

        # Create textarea for iterations display
        self.steps_display = QtWidgets.QPlainTextEdit(self)
        font_ = self.steps_display.font()
        font_.setPointSize(12)
        self.steps_display.setFont(font_)
        # Set tab width to 4 spaces
        self.steps_display.setTabStopDistance(
            QtGui.QFontMetricsF(font_).horizontalAdvance(' ') * 4)
        self.steps_display.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.steps_display.setReadOnly(True)

        # Create clear button
        self.clear_button = QtWidgets.QPushButton('Clear', self)
        self.clear_button.clicked.connect(self._on_click_clear)

        # Create info button
        self.info_button = QtWidgets.QPushButton('Info', self)
        self.info_button.clicked.connect(self._on_click_info)

        # Add widgets to window
        h_box_top = QtWidgets.QHBoxLayout()
        h_box_top.addWidget(self.input_box)
        h_box_top.addWidget(self.start_button)
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box_top)
        v_box.addWidget(self.steps_label)
        v_box.addWidget(self.steps_display)
        h_box_bottom = QtWidgets.QHBoxLayout()
        h_box_bottom.addStretch()
        h_box_bottom.addWidget(self.clear_button)
        h_box_bottom.addWidget(self.info_button)
        v_box.addLayout(h_box_bottom)
        # Central widget
        central = QtWidgets.QWidget(self)
        central.setLayout(v_box)
        self.setCentralWidget(central)
        self.show()
        self.input_box.setFocus()

    def _sequence(self, number):
        """Perform a recursive check with the Collatz sequence
        and print each step to `stepsDisplay`.

        Raises `Exception` and terminates if the `number` is 1.
        """

        self.steps_display.insertPlainText(str(number))
        if number == 1:
            self.steps_display.insertPlainText('\n')
        else:
            self.counter += 1
            if number % 2 == 0:
                self.steps_display.insertPlainText('\t| /2\n')
                self._sequence(int(number / 2))
            else:
                self.steps_display.insertPlainText('\t| *3 + 1\n')
                self._sequence(int(3 * number + 1))

    @ QtCore.pyqtSlot()
    def _on_click_start(self):
        """Clear the `stepsDisplay` and start the Collatz sequence."""

        self.steps_display.clear()
        try:
            input_value = int(self.input_box.text())
        except ValueError:
            # Empty input - ignore
            return
        self.counter = 0
        self._sequence(input_value)
        self.steps_display.insertPlainText(
            f'Terminated after {self.counter} iterations.')
        self.steps_display.moveCursor(QtGui.QTextCursor.End)

    @ QtCore.pyqtSlot()
    def _on_click_clear(self):
        """Clear the `inputBox` and `stepsDisplay`."""

        self.input_box.clear()
        self.steps_display.clear()
        self.input_box.setFocus()

    @ QtCore.pyqtSlot()
    def _on_click_info(self):
        """Open a dialog window to acces the relevant Wikipedia article."""

        if BrowserDialog(self).exec():
            webbrowser.open('https://en.wikipedia.org/wiki/Collatz_conjecture')
        else:
            self.input_box.setFocus()
