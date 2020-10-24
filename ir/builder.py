"""
"""

class Builder:
    def __init__(self, module):
        self.module = module
        self.lib = module.lib

    def i32(self):
        return self.lib.type_int32()

    def local_get(self, index, ty):
        return self.lib.local_get(self.module, index, ty)

    def param_ty(self, tys):
        tys = (tys[0] * len(tys))(*tys)
        return self.lib.type_create(tys, len(tys))

    def add_int32(self, a, b):
        return self.lib.binary(self.module, self.lib.add_int32(), a, b)

    def function(self, name, param_ty, result_ty, expr):
        return self.lib.add_function(self.module, name, param_ty, result_ty, None, 0, expr)
