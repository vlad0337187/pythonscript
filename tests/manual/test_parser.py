"""Contains tests on numbers.
"""

import os, os.path
from os.path import join, abspath
import sys
import ast
from ast import Module, ImportFrom, alias  # maybe to remove 'Module'

files_dir = os.path.dirname(__file__)
pythonscript_dir = os.path.abspath(os.path.join (files_dir, '../../'))
sys.path.insert(0, pythonscript_dir)

from scanner.scanner import tokenize
from parser.parser import Parser


def test_number_test():
    our_expression = '''
3 + 2 ** - 4 - - 1
a = 4
a == 4
a === 4
some_function()
    '''
    test_line_bounds_detection = '''
5 + 4
(a + 5)
'''
    current_code = our_expression

    print('source code was:')
    print(current_code)
    tokens = tokenize(current_code)
    for token in tokens: print(token.name, token.text)
    parser = Parser(tokens)
    node_tree = parser.parse_block()


test_number_test()
