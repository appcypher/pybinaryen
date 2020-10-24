#! /usr/bin/env pipenv run python

from ir import Module, Builder

def main():
    module = Module()
    builder = Builder(module)
    param_ty = None
    result_ty = None
    func = builder.function("test", param_ty, result_ty, None)
    # print(str(m))


if __name__ == "__main__":
    main()
