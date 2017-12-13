"""Contains all connected with parsing statements.
"""

import ast


def parse_statement(self):
    """Detects type of statement, parses it, returns AST node.
    """
    if self.current_token.name == 'IMPORT':
        statement = self.parse_import_statement()
        return statement


def parse_import_statement(self):
    self.expect('IMPORT')
    name = self.get_name()
    alias_node = ast.alias(name, name)
    import_node = ast.Import([alias_node], lineno=self.get_current_line(), col_offset=self.get_current_column())
    #self.next_token()
    return import_node
