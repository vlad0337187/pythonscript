"""Tests right detecting bounds of expressions, which are represented  by lines
    (inline and general).
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


def test_bounds_simple():
    """Tests detecting by parser bounds of lines, general and inline.
    Here are only simple cases, to be sure "Parser.find_end_of_line()" works well.
    """

    def find_and_print_eol(parser, line_type):
        """Searches for the end of current line.
        Requires parser to be on the first token of line.
        """
        token_start, token_end = parser.find_end_of_line(line_type)
        return token_start, token_end

    def print_debug_info():
        """Prints debug info, raises assertation error to output it.
        """
        nonlocal tokens, token_start, token_end

        for token in tokens: print(token.name, token.text)
        print(f'end of current line: {token_start}, {token_end}')
        #assert False

    code = '''
5 + 4
(a + 5)
5 + 4 (7 ** 18)
'''

    tokens = tokenize(code)
    parser = Parser(tokens)

    # line: "5 + 4"
    parser.set_current_token(1)
    token_start, token_end = find_and_print_eol(parser, 'general')
    assert token_start == 1
    assert token_end == 4

    # line: "(a + 5)"
    # details:
    #     general line must be finished on '\n'
    #     even if it contains only one inline line
    parser.set_current_token(5)
    token_start, token_end = find_and_print_eol(parser, 'general')
    assert token_start == 5
    assert token_end == 10

    # line: "(a + 5)"
    # details:
    #     Same line, but inline must be finished on ')'
    parser.set_current_token(5)
    token_start, token_end = find_and_print_eol(parser, 'inline')
    assert token_start == 5
    assert token_end == 9

    # line: "5 + 4 (7 ** 18)"
    parser.set_current_token(11)
    token_start, token_end = find_and_print_eol(parser, 'general')
    assert token_start == 11
    print_debug_info()
    assert token_end == 19

    # line: "5 + 4 (7 ** 18)"
    # details:
    #     if parser's told that current general line starts from middle of line,
    #     it must go to the end of line and parse it correctly
    parser.set_current_token(14)
    token_start, token_end = find_and_print_eol(parser, 'general')
    assert token_start == 14
    print_debug_info()
    assert token_end == 19

    # line: "5 + 4 (7 ** 18)"
    # details:
    #     if parser's told that current inline line starts from middle of line,
    #     it must go to the end of inline line and parse it correctly
    parser.set_current_token(14)
    token_start, token_end = find_and_print_eol(parser, 'inline')
    assert token_start == 14
    print_debug_info()
    assert token_end == 18
