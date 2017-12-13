"""
TODO:
    I passed (left on later) such functions in valagenieparser.vala:
        parse_literal
        parse_file
    Figure out:
        skip_symbol_name: do I need to add there skipping numbers / names
    Write:
        all methods in parse_methods_data.py
"""

import os, os.path
import sys
import ast

from . import errors


def find_method_modules():
    files_dir = os.path.dirname(__file__)
    appropriate_module_names = [mn.replace('.py', '') for mn in os.listdir(files_dir) if mn.startswith('methods_') if mn.endswith('.py')]
    return appropriate_module_names
method_modules = find_method_modules()

for mn in method_modules: exec(f'from . import {mn}')


class Parser:
    def __init__(self, tokens, filename=None):
        self.tokens = tokens
        self.current_token_index = 0  # index of current token
        self.last_token_index = len(tokens) - 1
        self.current_token = tokens[0]
        self.filename = filename

    def parse(self):
        """Parses self.tokens to AST tree, returns it.
        """
        all_nodes = self.parse_block()
        module = ast.Module(body=all_nodes)
        return module

    def raise_parse_error(self, expected):
        raise errors.ParseError(f'Error. File: {self.filename}. Expected any of {expected}, got {self.current_token.show_details()}')

    def raise_expected_name(self):
        raise errors.ParseError(f'Error. File: {self.filename}. Expected name, got {self.current_token.show_details()}')


def assing_methods_to_parser():
    for mn in method_modules:
        for attr_name in dir(eval(mn)):
            attribute = eval(mn + '.' + attr_name)
            if callable(attribute) and not attr_name.startswith('_'):
                setattr(Parser, attr_name, attribute)
            elif attr_name.isupper():
                setattr(Parser, attr_name, attribute)
assing_methods_to_parser()
