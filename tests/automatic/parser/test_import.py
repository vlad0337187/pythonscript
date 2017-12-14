"""Tests import statement
"""

import ast

from scanner.scanner import tokenize
from parser.parser import Parser


source_code = '''
import os
import os,sys
import os as osos, sys
import os as sosos,sys as sysys

import os sys as sysys
import os as oso   sys
import os as oso   sys as soso,types,ast
import os.path
import os.path as ospather   sys as soso,types,ast   os.path.dirname as dirname
'''


def test_import_1():
    code_1 = 'import os'
    expected_ast_node = ast.Import(ast.alias(name='os', asname=None))
    tokens = tokenize(source_code)
    parser = Parser(tokens)
    module = parser.parse()
    ast_node = ast.dump(module)
    assert expected_ast_node == ast_node
