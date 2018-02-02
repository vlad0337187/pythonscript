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

import ast
import importlib
import os, os.path
import sys

from . import errors


class Parser:
    ignored_tokens = ['{', '}']  # needed for visual highlighting
    # move ^ to "represent.py"

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
            node = self.parse_line()  # method placed in "method_blocks.py" too
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


def add_methods_to_parser():
    """Finds all methods for parser, which are placed in separate files.
    """
    global Parser

    def find_method_modules():
        """Finds and returns all module names in this file's folder, which start
        from '_methods'.
        """
        files_dir = os.path.dirname(__file__)
        appropriate_module_names = [mn.replace('.py', '') for mn in os.listdir(files_dir) if mn.startswith('methods_') if mn.endswith('.py')]
        return appropriate_module_names

    def assign_methods_to_parser():
        """Assigns all methods (callables), found in .py files of current directory,
        which start from 'methods_'.
        """
        nonlocal method_modules, method_modules_names

        for mn in method_modules_names:
            for attr_name in dir(method_modules[mn]):
                attribute = getattr(method_modules[mn], attr_name)
                if callable(attribute) and not attr_name.startswith('_'):
                    setattr(Parser, attr_name, attribute)
                elif attr_name.isupper():
                    setattr(Parser, attr_name, attribute)

    cur_package_name = __name__.split('.')[0]
    method_modules_names = find_method_modules()
    method_modules = {}

    for mn in method_modules_names: method_modules[mn] = importlib.import_module('.' + mn, cur_package_name)
    # for mn in method_modules_names: print(f'found {mn}')  # for testing
    assign_methods_to_parser()


add_methods_to_parser()
