"""Containds technical methods that will be used in Parser class.
All functions here will be used as methods, so they all have 'self' as first
argument.
"""

from . import represent
from .errors import ParseError


def next_token(self):
    self.current_token_index += 1
    self.current_token = self.tokens[self.current_token_index]


def previous_token(self):
    self.current_token_index += 1
    self.current_token = self.tokens[self.current_token_index]


def set_current_token(self, index):
    self.current_token_index = index
    self.current_token = self.tokens[index]


def get_current_line(self):
    return self.current_token.starts[0]


def get_current_column(self):
    return self.current_token.starts[1]


def find_end_of_line(self, line_type):
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
    return line_start, line_end
