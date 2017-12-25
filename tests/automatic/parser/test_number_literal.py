"""Contains tests on numbers.
"""

import os, os.path
from os.path import join, abspath
import sys
import ast
from ast import Module, ImportFrom, alias  # maybe to remove 'Module'

pythonscript_dir = os.environ['PYTHONSCRIPT_DIR']
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
    '''

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)
