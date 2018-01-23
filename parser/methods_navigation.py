"""Containds technical methods that will be used in Parser class.
All functions here will be used as methods, so they all have 'self' as first
argument.
"""


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


def find_end_of_line(self):
    """Finds the end of general or logical line.
    If it's a general line - than current token must be the first token from
    this line,
    if it's logical line, current token must be on an opening bracket "("
    for this logical line.
    """
    current_position = 
