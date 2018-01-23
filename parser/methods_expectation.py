"""Contains functions that probably or expect something.
Probably - means that if current token has given type - it goes to next token and returns True,
    otherwise - returnes False.
Expect - means that if current token has given type - it goes to next token and returns True,
    otherwise - raises Exception
Is - means that if current token has given type - returns True, otherwise - False.
Line is - means if line has given type - returns True, otherwise - False.
Get - means if token has given type - returns it's value, otherwise - raises error.
Detect line - detects type of given line, returns it.
"""

from . import represent


def probably(self, token_name):
    """Token name - neme, specified in TOKENS_DICT as key,
    or in Token class as 'name' parameter.
    """
    if self.current_token.name == token_name:
        self.next_token()
        return True
    else:
        return False


def probably_name(self):
    if self.current_token.name == 'NAME':
        self.next_token()
        return True
    else:
        return False


def probably_separator(self):
    if self.current_token.name in ['COMMA']:
        self.next_token()
        return True
    else:
        return False


def probably_eol(self):
    if self.current_token.name in ['SEMICOLON', 'EOL']:
        self.next_token()
        return True
    else:
        return False


def probably_indent(self):
    if self.current_token.name == 'INDENT':
        self.next_token()
        return True
    else:
        return False


def probably_block_start(self):
    if probably_eol():
        if probably_indent():
            return True
        else:
            self.previous_token()
    elif probably('RARROW'):
        return True
    else:
        return False


def expect(self, token_name):
    if self.probably(token_name):
        return True
    else:
        self.raise_parse_error(expected=token_name)


def expect_eol(self):
    if self.probably_eol():
        return True
    else:
        self.raise_parse_error(expected="''EOL' or 'SEMICOLON'")


def expect_name(self):
    if self.probably_name():
        return True
    else:
        self.raise_expected_name()


def expect_unary_operator(self):
    pass


def expect_binary_operator(self):
    pass


def line_is_comment(self):
    """Checks current and next tokens to detect: is it a comment, or not
    Often is used on a start of line to detect: does it containg
        comment, or expression, or statement
    """
    if self.current_token.name == '#':
        return True
    else:
        return False


def line_is_statement(self):
    """Checks current and next tokens to detect: is it expression, or not
    Often is used on a start of line to detect: does it has expression or statement
    """
    if self.current_token.name in ['NAME', 'IMPORT', 'FROM',
        'FUNCTION', 'RETURN', 'YIELD', 'GLOBAL', 'NONLOCAL', 'ASYNC', 'AWAIT',
        'CLASS',
        'FOR', 'WHILE', 'IF', 'SWITCH',
        'TRY', 'RAISE', 'ASSERT', 'WITH', 'DEL',
    ]:
        if self.current_token.name == 'NAME':
            # special case, can be statement, if "=" will be met ln line,
            # otherwise it's exression
            cur_position = self.current_token_index
            if self.probably('EOL'):
                self.set_current_token(cur_position)
                return False
            else:
                return True
        return True
    else:
        return False


def line_is_expression(self):
    """Checks current and next tokens to detect: is it expression, or not.
    Often is used on a start of line to detect: does it has expression or statement
    TODO:
        make check: does it starts from 'def', or number, or string, by this
            to check and give decision.
    """
    if self.current_token.name in ['NAME', 'NUMBER', 'STRING'].extend(operators.UNARY_OPERATORS):
        return True
    else:
        return False


def is_name(self):
    """If current token has type name, returns True, otherwise - False
    """
    if self.current_token.name == 'NAME':
        return True
    else:
        return False


def is_string_literal(self):
    pass


def is_number_literal(self):
    pass


def get_name(self):
    """If current token has type name, returns it, otherwise - raises ParseError.
    Swithes to next token.
    """
    if self.current_token.name == 'NAME':
        text = self.current_token.text
        self.next_token()
        return text
    else:
        self.raise_expected_name()


def detect_data_type(self):
    """Wrapper over is_expression(), is_statement(), is_comment()
    Detects near data type (starting from current token)
    Often is used on a start of line to detect: does it has expression or statement
    If current token is name:
        if next token is '=' - it's statement
    """
