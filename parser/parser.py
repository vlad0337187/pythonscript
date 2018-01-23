"""
TODO:
    I passed (left on later) such functions in valagenieparser.vala:
        parse_literal
        parse_file
    Figure out:
        skip_symbol_name: do I need to add there skipping numbers / names
    Write:
        all methods in parse_methods_data.py
    Add to README.md:
        '==' is synonim to 'is', '===' checks: is it the same object
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
    ignored_tokens = ['{', '}']  # needed for visual highlighting

    def __init__(self, tokens, filename=None):
        self.tokens = tokens
        self.current_token_index = 0  # index of current token
        self.last_token_index = len(tokens) - 1
        self.current_token = tokens[0]
        self.filename = filename
        self.remove_ignored_tokens()

    def parse(self, mode='module'):
        """Parses self.tokens to AST tree, returns it.
        """
        if mode == 'module':
            nodes = self.parse_block()
            module = ast.Module(body=nodes)
            return module
        elif mode == 'block':
            nodes = self.parse_block()
            return nodes
        elif mode == 'line':
            node = self.parse_line()
            return node
        else:
            raise ValueError(f'Unsupported mode: {mode}')


    def remove_ignored_tokens(self):
        """Removes ignored tokens from tokenlist.
        """
        new_tokenlist = []
        for token in self.tokens:
            if token not in self.ignored_tokens:
                new_tokenlist.append(token)
        self.tokens = new_tokenlist

    def raise_parse_error(self, expected):
        raise errors.ParseError(f'Error. File: {self.filename}. Expected any of {expected}, got {self.current_token.show_details()}')

    def raise_expected_name(self):
        raise errors.ParseError(f'Error. File: {self.filename}. Expected name, got {self.current_token.show_details()}')


def assign_methods_to_parser():
    """Assigns all methods, found in .py files of current directory,
    which start from 'methods_'
    """
    for mn in method_modules:
        for attr_name in dir(eval(mn)):
            attribute = eval(mn + '.' + attr_name)
            if callable(attribute) and not attr_name.startswith('_'):
                setattr(Parser, attr_name, attribute)
            elif attr_name.isupper():
                setattr(Parser, attr_name, attribute)
assign_methods_to_parser()
