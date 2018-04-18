"""Contains all connected with parsing statements.
"""

import ast


def parse_statement(self):
    """Detects type of statement, parses it, returns AST node.
    """
    if self.current_token.name == 'IMPORT':
        statement = self.parse_import_statement()
        return statement
    elif self.current_token.name == 'FROM':
        statement = self.parse_from_import_statement()
        return statement


def parse_from_import_statement(self):
    """Parses statement of such view: 'from os import path'.
    Uses:
        'parse_import_statement'
    """
    self.expect('FROM')

    relative_import_level = self.count_amount_of_dots()
    from_what = self.get_name_with_dots()

    import_statement = self.parse_import_statement()
    from_import_statement = ast.ImportFrom(module=from_what, names=import_statement.names,
            level=relative_import_level,
            lineno=import_statement.lineno, col_offset=import_statement.col_offset)

    return from_import_statement



def parse_import_statement(self):
    """Parses such statements: 'import os'
    """
    self.expect('IMPORT')
    what_to_import = []
    while True:
        name = self.get_name_with_dots()

        if self.probably('COMMA'):
            what_to_import.append(ast.alias(name, None))
            continue
        elif self.probably('AS'):
            alias_name = self.get_name()
            what_to_import.append(ast.alias(name, alias_name))
            if self.probably('COMMA') or self.is_name():
                continue
            elif self.expect_eol():
                break
        elif self.is_name():
            what_to_import.append(ast.alias(name, None))  # append previous and go to next
            continue
        else:
            what_to_import.append(ast.alias(name, None))
            self.expect_eol()
            break

    import_node = ast.Import(names=what_to_import, lineno=self.get_current_line(), col_offset=self.get_current_column())
    return import_node
