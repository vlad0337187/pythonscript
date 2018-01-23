"""Tests import statement
"""

import os, os.path
from os.path import join, abspath
import sys
import ast
from ast import Module, Import, alias  # maybe to remove 'Module'

pythonscript_dir = os.environ['PYTHONSCRIPT_DIR']
sys.path.insert(0, pythonscript_dir)

from scanner.scanner import tokenize
from parser.parser import Parser


def test_import_1():
    code_1 = 'import os'

    expected_ast_node = ast.Import(names=[ast.alias(name='os', asname=None)])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_2():
    code_1 = 'import os,sys'

    expected_ast_node = Import(names=[alias(name='os', asname=None), alias(name='sys', asname=None)])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_3():
    code_1 = 'import os as osos, sys'

    expected_ast_node = Import(names=[alias(name='os', asname='osos'), alias(name='sys', asname=None)])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    print('Tokens:')
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    print('ast_node_string:', ast_node_string)
    print('expected_ast_node_string', expected_ast_node_string)
    assert ast_node_string == expected_ast_node_string


def test_import_4():
    code_1 = 'import os as sosos,sys as sysys'

    expected_ast_node = Import(names=[alias(name='os', asname='sosos'), alias(name='sys', asname='sysys')])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_5():
    code_1 = 'import os sys as sysys'

    expected_ast_node = Import(names=[alias(name='os', asname=None), alias(name='sys', asname='sysys')])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_6():
    code_1 = 'import os as oso   sys'

    expected_ast_node = Import(names=[alias(name='os', asname='oso'), alias(name='sys', asname=None)])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_7():
    code_1 = 'import os as oso   sys as soso,types,ast'

    expected_ast_node = Import(names=[
        alias(name='os', asname='oso'),alias(name='sys', asname='soso'),
        alias(name='types', asname=None), alias(name='ast', asname=None)
        ])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_8():
    code_1 = 'import os.path'

    expected_ast_node = Import(names=[alias(name='os.path', asname=None)])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_import_9():
    code_1 = 'import os.path as ospather   sys as soso,types,ast   os.path.dirname as dirname'

    expected_ast_node = Import(names=[
        alias(name='os.path', asname='ospather'),alias(name='sys', asname='soso'),
        alias(name='types', asname=None), alias(name='ast', asname=None),
        alias(name='os.path.dirname', asname='dirname'),
        ])
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string
