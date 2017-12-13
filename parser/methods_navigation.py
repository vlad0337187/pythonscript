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
