"""
"""


class LoadError(Exception):
    """ Represents the error raised from loading a library """

    def __init__(self, message):
        super().__init__(message)
        self.message = message  # Added because it is missing after super init

    def __repr__(self):
        return f'ParserError(message="{self.message}")'
