"""This module contains real 'pythonscript's test functions rewrited into
Pythonscript.
"""


"""Tests 'from import' statement
"""

import os os.path
from os.path import join abspath
import sys
import ast
from ast import ImportFrom alias

pythonscript_dir = os.environ['PYTHONSCRIPT_DIR']
sys.path.insert(0, pythonscript_dir)

from scanner.scanner import tokenize
from parser.parser import Parser




#####################
######## Python Code:

def test_from_import_1():
    code_1 = 'from os import path'

    expected_ast_node = ImportFrom(module='os', names=[alias(name='path', asname=None)], level=0)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


#####################
## PythonScript Code:

function test_from_import_1
    code_1 = 'from os import path'

    expected_ast_node = ImportFrom module='os' names=list alias name='path' asname=None; level=0
    expected_ast_node_string = ast.dump expected_ast_node

    tokens = tokenize code_1
    for token in tokens -> print token.name, token.text

    parser = Parser tokens
    ast_node = parser.parse mode='line'
    ast_node_string = ast.dump ast_node

    assert ast_node_string == expected_ast_node_string




#####################
######## Python Code:

def some_extra_test():
    func_1 = func_2(arg_1, arg_2(func_3(arg_3)))


#####################
## PythonScript Code:

function some_extra_test
    func_1 = func_2 arg_1 arg_2 (func_3 arg_3)




#####################
######## Python Code:

deleted_sections = SomeModel.objects.all_by_order().filter(place='some_place').exclude(have_some_prop=None)


#####################
## PythonScript Code:

deleted sections = Section.objects.all_by_order().filter(place='some_place').exclude(havesome_prop=None)

# or:

deleted sections = Section.objects
    .all_by_order()
    .filter place='some_place'
    .exclude havesome_prop=None




#####################
######## Python Code:

NewClass(arg1, arg2, func1(arg3)).some_method().some_method_2()


#####################
## PythonScript Code:

NewClass arg1 arg2 (func1 arg3)
    .some_method()    # requires indent
    .some_method_2()




#####################
######## Python Code:

a = [a, b, c, 14, 228, 563].reverse()


#####################
## PythonScript Code:

a = list a b c 14 228 563
    .reverse()




#####################
######## Python Code:
# More bound case:

a = [a, b, c, 14, 228, 563].reverse().extend(
    [7, 8, 9, 10, 12, somevariable].reverse()
)


#####################
## PythonScript Code:
# More bound case:

a = list a b c 14 228 563
    .reverse()
    .extend list 7 8 9 10 12 somevariable
        .reverse()
