"""Contains methods for parsing main expressions.
Methods for particular cases are placed in separate files.
"""

from . import represent


def parse_expression(self):
    """Detects type of expression, parses it, returns AST node.
    """
    line_start, line_end = self.find_end_of_expression_line()
    self.set_current_token(line_end)
    self.next_token()
    return 'EOL'
    while True:  # we wait end of logic line (same as end of expression)
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


def find_end_of_expression_line(self, line_type='general'):
    """Finds the end of general or logical line.
    If it's a general line - than current token must be the first token from
    this line,
    if it's logical line, current token must be on an opening bracket "("
    for this logical line.
    Arguments:
        - line_type: 'general' or 'inline'
    """
    line_start = self.current_token_index
    line_end = None

    if (self.current_token.name in represent.EOL_TOKENS) and line_type == 'general':  # empty line
        return line_start, line_start

    opened_sublines = 0

    if self.current_token.name == 'LPAR' and line_type == 'general':
        # special case when subline is in start of general line
        opened_sublines += 1

    while True:  # waiting end of this line
        self.next_token()

        if line_type == 'general':
            if self.is_eol() and opened_sublines == 0:
                line_end = self.current_token_index
                break
        elif line_type == 'inline':
            if self.is_type('RPAR') and opened_sublines == 0:
                line_end = self.current_token_index
                break

        print('line was not finished')
        print(f"current token: {self.current_token.name}, it's index: {self.current_token_index}")

        if self.current_token.name == 'LPAR':
            opened_sublines += 1
            continue

        if self.current_token.name == 'RPAR':
            if opened_sublines >= 0:
                opened_sublines -= 1
                continue
            else:
                raise ParseError("It's general line, there were no opening parenthesises,\
so closing parenhesis can't be placed here.")

    print(f'met {line_type} line, started on {line_start}, finished on {line_end}')
    self.set_current_token(line_start)
    return line_end
