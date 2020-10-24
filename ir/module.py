
"""
"""

from .lib import Lib

class Module:
    """
    Module encapsulates a Binaryen module which owns all objects passed to it.
    """
    def __init__(self):
        self.lib = Lib()
        self.module = self.lib.module_create()

    # def __del__(self):
    #     # Free module
    #     self.lib.module_dispose(self.module)

    def __str__(self):
        return self.lib.module_print(self.module)

    def add_function(self, func):
        pass
