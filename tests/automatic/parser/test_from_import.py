"""Tests 'from import' statement
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


def test_from_import_2():
    code_1 = 'from os import path as dirname, abspath'

    expected_ast_node = ImportFrom(module='os', names=[alias(name='path', asname='dirname'), alias(name='abspath', asname=None)], level=0)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='one_line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_from_import_3():
    code_1 = 'from os.path import dirname abspath as bspth'

    expected_ast_node = ImportFrom(module='os.path', names=[alias(name='dirname', asname=None), alias(name='abspath', asname='bspth')], level=0)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='one_line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_from_import_4():
    code_1 = 'from os.path import dirname, abspath as bspth isrelative'

    expected_ast_node = ImportFrom(
        module='os.path', names=[
            alias(name='dirname', asname=None), alias(name='abspath', asname='bspth'),
            alias(name='isrelative', asname=None)
            ],
        level=0)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='one_line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_from_import_5():
    code_1 = 'from .os.path import dirname'

    expected_ast_node = ImportFrom(module='os.path', names=[alias(name='dirname', asname=None)], level=1)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='one_line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_from_import_6():
    code_1 = 'from ....os.path import dirname as dr2, abspath'

    expected_ast_node = ImportFrom(
        module='os.path',
        names=[alias(name='dirname', asname='dr2'), alias(name='abspath', asname=None)],
        level=4)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='one_line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string


def test_from_import_6():
    code_1 = 'from ...os.path import dirname as dr2 abspath isdir'

    expected_ast_node = ImportFrom(
        module='os.path',
        names=[
            alias(name='dirname', asname='dr2'), alias(name='abspath', asname=None),
            alias(name='isdir', asname=None)],
        level=3)
    expected_ast_node_string = ast.dump(expected_ast_node)

    tokens = tokenize(code_1)
    for token in tokens: print(token.name, token.text)

    parser = Parser(tokens)
    ast_node = parser.parse(mode='one_line')
    ast_node_string = ast.dump(ast_node)

    assert ast_node_string == expected_ast_node_string
