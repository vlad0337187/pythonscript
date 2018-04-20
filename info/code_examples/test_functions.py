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
    ast_node = parser.parse(mode='one_line')
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
    ast_node = parser.parse mode='one_line'
    ast_node_string = ast.dump ast_node

    assert ast_node_string == expected_ast_node_string








#####################
######## Python Code:

def some_extra_test(arg_1, arg_2, arg_3, func_3):
    func_1 = func_2(arg_1, arg_2(func_3(arg_3)))


#####################
## PythonScript Code:

def arg_1, arg_2, arg_3, func_3
    func_1 = func_2 arg_1 arg_2 (func_3 arg_3)

# or:

function(some_extra_test)       # space before '(' is optional
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
    .some_object
    .filter place='some_place'
    .exclude havesome_prop=None








#####################
######## Python Code:

NewClass(arg1, arg2, func1(arg3)).some_method().some_method_2()


#####################
## PythonScript Code:

NewClas arg1, arg2, func1(arg3)
    .some_method()
    .some_method_2()

# or:

NewClas arg1 arg2 func1(arg3)
    .some_method()
    .some_method_2()








# if you call some function, you can pass arguments to it without commas
# but if you already pass arguments and want to pass as argument
# called with some argument function - than you must place it into









expected_ast_node = ImportFrom(module='os', names=[alias(name='path', asname=None)], level=0).some_method().some_method_2(arg1, arg2, 324)


expected_ast_node = ImportFrom
    module='os' names=list alias name='path' asname=None; level=0
        .some_method ()
        .some_method_2
            arg, arg2, 324

# after indent if name starts from '.' - it's attribute taking,
# if without - it means calling with passing arguments
#
# if newline - continuing taking attributes or passing attributs for object
# calling,
# if indent - all same, but only for curent object before indent








#####################
######## Python Code:

a = [a, b, c, 14, 228, 563].reverse()


#####################
## PythonScript Code:

a = list a b c 14 228 563
    .reverse()

# but this would give an error:
a = list a b c 14 228 563
    reverse()
# , because calling lists is impossible,
# also, probably, there's no such function 'reverse'







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








#####################
######## Python Code:

a = lambda x, y: x + y


#####################
## PythonScript Code:

a = def x, y -> return x + y <-
