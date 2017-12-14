#! /usr/bin/python3
"""Tests 'from import' statement.
"""


import os
import os.path
import sys
import ast
import types

files_dir = os.path.dirname(__file__)
pythonscript_dir = os.path.abspath(os.path.join (files_dir, '../'))
sys.path.insert(0, pythonscript_dir)

from scanner.scanner import tokenize
from parser.parser import Parser


source_code = """
from os import path
from os import path as dirname, abspath
from os.path import dirname abspath as bspth

from os.path import dirname, abspath as bspth isrelative

from .os.path import dirname
from ....os.path import dirname
"""


if __name__ == '__main__':
    tokens = tokenize(source_code)
    print()
    print('Received tokens:')
    for token in tokens:
        print(token.name, token.text)
    parser = Parser(tokens)
    module = parser.parse()
    print()
    print('Parsing result:')
    print(ast.dump(module))
    result = compile(module, '<test source code>', mode='exec')
    print('type of result after compilitg: ', type(result))
    result = types.ModuleType('test_module', result)
    print('type of result after creating module: ', type(result))
    sys.modules['test_module'] = result
    import test_module
    print(dir(test_module))
    #print(getattr(result, 'os'))
