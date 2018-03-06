"""Contains tests for detecting content type inside of line: is it statement,
or expressions, or comment.

Tests next methods:
    .line_is_comment()
    .line_is_statement()
    .line_is_expression()
    .line_is_empty()
    .detect_line_type()
"""


import os, os.path
from os.path import join, abspath
import sys
import ast
from ast import Module, ImportFrom, alias  # maybe to remove 'Module'

# remove this after manual testing <<<<
files_dir = os.path.dirname(__file__)
if files_dir.startswith('.'):  # is relative
    cwd = os.getcwd()
    files_dir = abspath(join(cwd, files_dir))

ps_dir = os.path.abspath(os.path.join(files_dir, '../../../'))
os.environ['PYTHONSCRIPT_DIR'] = ps_dir
# end of remove  <<<<<

pythonscript_dir = os.environ['PYTHONSCRIPT_DIR']
sys.path.insert(0, pythonscript_dir)

from scanner.scanner import tokenize
from parser.parser import Parser


def test_line_type_simple():
    """Tests detecting of basic lines with different line types.
    """
    code = '''
5 + 4

(a + 5)
a = 3
fn a b -> a + b

# some comment
some_variable_name

def a():
return some_war
yield 4 + 4

if x == 4
switch some_name

import os, sys
from some_module import some_variable

try
raise ValueError

'''

    code_with_descriptions = '''
5 + 4                                                           # from 1  to 4

(a + 5)                                                         # from 6  to 11
a = 3                                                           # from 12 to 15
fn a b -> a + b                                                 # from 16 to 23

# some comment                                                  # from 25 to 26
some_variable_name                                              # from 27 to 28

def a()                                                         # from 30 to 34
return some_war                                                 # from 35 to 37
yield 4 + 4                                                     # from 38 to 42

if x == 4                                                       # from 44 to 48
switch some_name                                                # from 49 to 51

import os, sys                                                  # from 53 to 57
from some_module import some_variable                           # from 58 to 62

try                                                             # from 64 to 65
raise ValueError                                                # from 66 to 68


5 + 4     # starts from token with index 1, ends with index 4

(a + 5)    #  with index 6, ends with index 11
a = 3    # from index 12 to index 15

# some comment    # from index 25, to index 26  (just comment)
def a():    # from index 27 to index 32

'''  # it's not used in code, just for convenience

    tokens = tokenize(code)
    parser = Parser(tokens)

    # Test .line_is_empty()
    assert parser.line_is_empty()
    parser.set_current_token(5)
    assert parser.line_is_empty()

    # Test .line_is_expression()
    parser.set_current_token(1)
    assert parser.line_is_expression()
    parser.set_current_token(6)  # start of "(a + 5)"
    assert parser.line_is_expression()
    parser.set_current_token(12)  # start of "a = 3"
    assert not parser.line_is_expression()

    # Test .line_is_statement()
    parser.set_current_token(12)
    assert parser.line_is_statement()
    parser.set_current_token(19)
    assert parser.line_is_statement()
