#! /usr/bin/python3


import os
import os.path
import sys
import ast

files_dir = os.path.dirname(__file__)
pythonscript_dir = os.path.abspath(os.path.join (files_dir, '../'))
sys.path.insert(0, pythonscript_dir)

from scanner.scanner import tokenize
from parser.parser import Parser


source_code = """
import os
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
    result
    print(result.os)
