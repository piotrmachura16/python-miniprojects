"""This module contains the arbitraryly big int validator."""
from PyQt5 import QtGui


class IntValidator(QtGui.QDoubleValidator):
    """Normal QIntValidator is limited to 32-bit signed size.
    This version utilizes QDoubleValidator to allow for arbitraryly big
    integers, which are possible in Python.
    """

    def __init__(self, bottom=float('-inf'), top=float('inf')):
        super(IntValidator, self).__init__(bottom, top, 0)
        self.setNotation(QtGui.QDoubleValidator.StandardNotation)

    def validate(self, text, pos):
        """Validate which disalows the '.' symbol."""
        # Disallow '.' symbol since only ints are allowed
        if text.endswith('.'):
            return QtGui.QValidator.Invalid, text, pos
        return super(IntValidator, self).validate(text, pos)
