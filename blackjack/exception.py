"""This module contains the custom Exception used to manage game flow"""


class BlackJackException(Exception):
    """The exception BlackJackException used to manage game flow. Contains a
    field `message` with the message to be displayed.
    """

    def __init__(self, message: str):
        super().__init__()
        self.messsage = message
