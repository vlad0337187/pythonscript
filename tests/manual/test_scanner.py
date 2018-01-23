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
    numbers_literals = '''
    # integers:
    423
    0
    # float numbers:
    56.52
    0.0
    # octal numbers:
    0o100    # == 64
    # hexadecimal numbers:
    0x40    # == 64
    # little numbers:
    0e2    # == 0.0
    # complex (imaginary) numbers:
    3.14e-10j
    '''
    different_literals = '''
    'test string'
    444
    b'test bytes string'
    4.0
    3.14e-10j
    '''
    other_code = '''
    3 ** 2
    a = 4
    b -= 3
    '''
    our_expression = '''
3 + 2 ** - 4 - - 1
a = 4
a == 4
a === 4
    '''

    tokens = tokenize(our_expression)
    for token in tokens: print(token.name, token.text)


test_number_test()
