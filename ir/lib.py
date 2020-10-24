"""
"""
import platform
from ctypes import (
    cdll,
    c_void_p,
    POINTER,
    Structure,
)
from .errors import LoadError


class Module(Structure):
    _fields_ = []


class Lib:
    """
    """

    def __init__(self):
        self.lib = Lib.load_library()
        self.ModuleRef = POINTER(Module)
        self.module_create = self.lib.BinaryenModuleCreate
        # self.module_create.restype = self.ModuleRef
        self.module_print = self.lib.BinaryenModulePrint
        self.module_dispose = self.lib.BinaryenModuleDispose
        self.type_int32 = self.lib.BinaryenTypeInt32
        self.type_create = self.lib.BinaryenTypeCreate
        self.local_get = self.lib.BinaryenLocalGet
        self.add_int32 = self.lib.BinaryenAddInt32
        self.add_function = self.lib.BinaryenAddFunction
        self.binary = self.lib.BinaryenBinary

    @staticmethod
    def load_library():
        """
        """

        os = platform.uname()[0]

        if os == "Windows":
            lib_name = "binaryen.dll"
        elif os == "Linux":
            lib_name = "libbinaryen.so"
        elif os == "Darwin":
            lib_name = "libbinaryen.dylib"
        else:
            raise LoadError("Cannot load library. Platform is currently not supported!")

        return cdll.LoadLibrary(lib_name)

