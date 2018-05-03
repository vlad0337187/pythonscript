"""Methods to find something in code.
For example, to find end of some expression, or end of file.
"""

from . import represent


def find_end_of_expression_line(self, line_type='general'):
    """Finds the end of general or logical line.
    If it's a general line - than current token must be the first token from
    this line,
    if it's logical line, current token must be on an opening bracket "("
    for this logical line.
    Arguments:
        - line_type: 'general' or 'inline'
    TODO:
        - maybe to rename 'inline' to 'scoped' ?
            anyway it means that line is in brackets, also (probably?),
            inside of parenthesises cannot be statement.
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


def find_end_of_statement_line(self):
    # TODO !!!!!!!!!!!!!! THIS
    # stopped on this
    # At first, I decided to implement expressions parsing,
    # than to return here
    statement_type = self.detect_statement_type()
