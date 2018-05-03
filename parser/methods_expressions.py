"""Contains methods for parsing main expressions.
Methods for particular cases are placed in separate files.
"""

from . import represent


def parse_expression(self):
    """Detects type of expression, parses it, returns AST node.
    """

    def pass_lpar_if_inline():
        """Just goes to next token if current one is LPAR '(' and line type is inline.
        """
        if expr_type == 'inline' and self.is_type('LPAR'):
            self.next_token()

    def pass_rpar_if_inline():
        """Just goes to next token if current one is RPAR ')' and line type is inline.
        """
        if expr_type == 'inline' and self.is_type('RPAR'):
            self.next_token()

    expr_type = self.detect_expression_type()
    line_start, line_end = self.find_end_of_expression_line(expr_type)

    pass_lpar_if_inline()

    #self.set_current_token(line_end)
    #self.next_token()
    #return 'EOL'

    while True:  # we wait end of logic line (same as end of expression)
        if self.current_token_index == line_end:
            pass_rpar_if_inline()
            break

        if self.current_token.name == 'DEF':
            pass  # parse inline function
        elif self.current_token.name == 'OBJ':
            pass  # parse inline class
        elif self.current_token.name in represent.UNARY_OPERATORS:
            pass
        elif self.current_token.name in represent.LITERALS:
            pass




def parse_attribute_access(self):
    """Parses access to attribute (such expression: 'var_1.attr_1')
    """
    pass
