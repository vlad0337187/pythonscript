"""Contains methods for parsing main expressions.
Methods for particular cases are placed in separate files.
"""

from . import represent


def parse_expression(self):
    """Detects type of expression, parses it, returns AST node.
    """
    while True:  # we wait end of logic line (same as end of expression)
        if self.current_token.name == 'DEF':
            pass  # parse inline function
        elif self.current_token.name == 'OBJ':
            pass  # parse inline class
        elif self.current_token.name in operators.UNARY_OPERATORS:
            pass
        elif self.current_token.name in operators.LITERALS:
            pass


def parse_attribute_access(self):
    """Parses access to attribute (such expression: 'var_1.attr_1')
    """
    pass
