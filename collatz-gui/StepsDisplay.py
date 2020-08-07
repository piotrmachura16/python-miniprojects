import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class StepsDisplay(QtWidgets.QPlainTextEdit):
    '''
    A read-only QPlainTextEdit with some additional tweaks.
    '''

    def __init__(self, parent):
        super(StepsDisplay, self).__init__(parent)
        # Set font size
        f = self.font()
        f.setPointSize(12)
        self.setFont(f)
        # Set tab width to 4 spaces
        self.setTabStopDistance(
            QtGui.QFontMetricsF(f).horizontalAdvance(' ') * 4)
        self.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.setReadOnly(True)
        self.insertPlainText('Steps:\n')

    def clear(self):
        '''
        Clear the field and add the 'Steps:\n' prompt
        '''
        super().clear()
        self.insertPlainText('Steps:\n')
