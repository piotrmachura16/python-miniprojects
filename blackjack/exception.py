"""This module contains the exceptions used to manage game flow"""
from player import Player


class BlackJackException(Exception):
    """The base BlackJackException used to manage game flow."""


class ExitException(BlackJackException):
    """Used to exit the game."""


class BustedException(BlackJackException):
    """Used to signify busting."""


class FoldException(BlackJackException):
    """Used to signify folding."""


class WinException(BlackJackException):
    """Used to signify winning."""

    def __init__(self, player: Player):
        super().__init__()
        self.winning_player = player
