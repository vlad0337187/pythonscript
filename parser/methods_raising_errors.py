"""Contains methods, which will raise different parsing errors.
"""


from . import errors


def raise_parse_error(self, expected):
    raise errors.ParseError(f'Error. File: {self.filename}. Expected any of {expected}, got {self.current_token.show_details()}')


def raise_expected_name(self):
    raise errors.ParseError(f'Error. File: {self.filename}. Expected name, got {self.current_token.show_details()}')


def raise_unknown_line(self):
    raise errors.ParseError(f'Error. File: {self.filename}. Cannot detect type of line on {self.current_token.show_details()}')
