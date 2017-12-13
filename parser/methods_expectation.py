"""Contains functions that probably or expect something.
Accept - means that if current token has given type - it goes to next token and returns True,
otherwise - returnes False.
Expects -
"""


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
        self.raise_parser_error()


def expect_name(self):
    if self.probably_name():
        return True
    else:
        self.raise_expected_name()


def expect_unary_operator(self):
    pass


def expect_binary_operator(self):
    pass


def is_expression(self):
    """Checks next tokens to detect: is it expression, or not.
    """
    pass


def is_statement(self):
    """Checks next tokens to detect: is it expression, or not.
    """
    if self.current_token.name in ['NAME', 'IMPORT', 'FROM',
        'FUNCTION', 'RETURN', 'YIELD', 'GLOBAL', 'NONLOCAL', 'ASYNC', 'AWAIT',
        'CLASS',
        'FOR', 'WHILE', 'IF', 'SWITCH',
        'TRY', 'RAISE', 'ASSERT', 'WITH', 'DEL',
    ]:
        if self.current_token.name == 'NAME':
            cur_position = self.current_token_index
            if self.probably('EOL'):
                self.set_current_token(cur_position)
                return False
        return True
    else:
        return False


def is_comment(self):
    pass


def is_name(self):
    """If current token has type name, returns True, otherwise - False
    """
    pass


def get_name(self):
    """If current token has type name, returns it, otherwise - raises ParseError.
    """
    if self.current_token.name == 'NAME':
        text = self.current_token.text
        self.next_token()
        return text
    else:
        self.raise_expected_name()


def is_string_literal(self):
    pass


def is_number_literal(self):
    pass
