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
    code_1 = '''
5 + 4

(a + 5)
fn a b -> a + b
some_variable_name
'''
    # line 2: from 1  to 4     #  5 + 4
    # line 4: from 6  to 11    #  (a + 5)
    # line 5: from 12 to 19    #  fn a b -> a + b
    # line 6: from 20 to 21    #  some_variable_name

    code_2 = '''
a = 3
def a():
return some_war
yield 4 + 4
if x == 4
switch some_name
try
raise ValueError
import os, sys
from some_module import some_variable
'''
    # line 2:  from 1  to 4     #  a = 3
    # line 3:  from 5  to 10    #  def a():
    # line 4:  from 11 to 13    #  return some_war
    # line 5:  from 14 to 18    #  yield 4 + 4
    # line 6:  from 19 to 23    #  if x == 4
    # line 7:  from 24 to 26    #  switch some_name
    # line 8:  from 27 to 28    #  try
    # line 9:  from 29 to 31    #  raise ValueError

    # line 10: from 32 to 36    #  import os, sys
    # line 11: from 37 to 41    #  from some_module import some_variable

    code_3 = '''
# some comment
    # some comment 2
'''
    # line 2:  from 1  to 2
    # line 3:  from 3  to 4

    # Helpful debug info:
    # (you can use them to debug functions)
    #print ('cur token: ', parser_2.current_token.name, parser_2.current_token.text)
    #print ('token context: ', parser_2.current_token.context)
    #[print (token.name) for token in tokens_2]

    tokens_1 = tokenize(code_1)
    parser_1 = Parser(tokens_1)

    tokens_2 = tokenize(code_2)
    parser_2 = Parser(tokens_2)

    tokens_3 = tokenize(code_3)
    parser_3 = Parser(tokens_3)

    # Test .line_is_empty()
    assert parser_1.line_is_empty()
    parser_1.set_current_token(5)
    assert parser_1.line_is_empty()

    # Test .line_is_expression()

    # True:
    parser_1.set_current_token(1)           # 5 + 4
    assert parser_1.line_is_expression()
    parser_1.set_current_token(6)           # (a + 5)
    assert parser_1.line_is_expression()
    parser_1.set_current_token(12)          # fn a b -> a + b
    assert parser_1.line_is_expression()
    parser_1.set_current_token(20)          # some_variable_name
    assert parser_1.line_is_expression()
    # False:
    parser_2.set_current_token(1)           # a = 3
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(5)           # def a():
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(11)          # return some_war
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(14)          # yield 4 + 4
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(19)          # if x == 4
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(24)          # switch some_name
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(27)          # try
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(29)          # raise ValueError
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(32)          # import os, sys
    assert not parser_2.line_is_expression()
    parser_2.set_current_token(37)          # from some_module import some_variable
    assert not parser_2.line_is_expression()

    # Test .line_is_statement()

    # True
    parser_2.set_current_token(1)           # a = 3
    assert parser_2.line_is_statement()
    parser_2.set_current_token(5)           # def a():
    assert parser_2.line_is_statement()
    parser_2.set_current_token(11)          # return some_war
    assert parser_2.line_is_statement()
    parser_2.set_current_token(14)          # yield 4 + 4
    assert parser_2.line_is_statement()
    parser_2.set_current_token(19)          # if x == 4
    assert parser_2.line_is_statement()
    parser_2.set_current_token(24)          # switch some_name
    assert parser_2.line_is_statement()
    parser_2.set_current_token(27)          # try
    assert parser_2.line_is_statement()
    parser_2.set_current_token(29)          # raise ValueError
    assert parser_2.line_is_statement()
    parser_2.set_current_token(32)          # import os, sys
    assert parser_2.line_is_statement()
    parser_2.set_current_token(37)          # from some_module import some_variable
    assert parser_2.line_is_statement()
    # False
    parser_1.set_current_token(1)           # 5 + 4
    assert not parser_1.line_is_statement()
    parser_1.set_current_token(6)           # (a + 5)
    assert not parser_1.line_is_statement()
    parser_1.set_current_token(12)          # fn a b -> a + b
    assert not parser_1.line_is_statement()
    parser_1.set_current_token(20)          # some_variable_name
    assert not parser_1.line_is_statement()

    # Test .detect_line_type()

    parser_1.set_current_token(1)           # 5 + 4
    assert parser_1.detect_line_type() == 'expression'
    parser_1.set_current_token(5)
    assert parser_1.detect_line_type() == 'empty'
    parser_1.set_current_token(6)           # (a + 5)
    assert parser_1.detect_line_type() == 'expression'
    parser_1.set_current_token(12)          # fn a b -> a + b
    assert parser_1.detect_line_type() == 'expression'
    parser_1.set_current_token(20)          # some_variable_name
    assert parser_1.detect_line_type() == 'expression'

    parser_2.set_current_token(1)           # a = 3
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(5)           # def a():
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(11)          # return some_war
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(14)          # yield 4 + 4
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(19)          # if x == 4
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(24)          # switch some_name
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(27)          # try
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(29)          # raise ValueError
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(32)          # import os, sys
    assert parser_2.detect_line_type() == 'statement'
    parser_2.set_current_token(37)          # from some_module import some_variable
    assert parser_2.detect_line_type() == 'statement'

    parser_3.set_current_token(1)
    assert parser_1.detect_line_type() == 'comment'
    parser_1.set_current_token(3)
    assert parser_1.detect_line_type() == 'comment'
