"""This module contains the custom Exception used to manage game flow"""
from player import Player

class BlackJackException(Exception):
    """The base BlackJackException used to manage game flow."""


class ExitException(BlackJackException):
    """The ExitException used to exit the game."""

class BustedException(BlackJackException):
    """The BustedException used to signify busting."""

class FoldException(BlackJackException):
    """The FoldException used to signify folding."""

class WinException(BlackJackException):
    """The exception used to signify winning."""
    def __init__(self, player: Player):
        super().__init__()
        self.winning_player = player
