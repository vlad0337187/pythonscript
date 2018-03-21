"""Contains functions that probably or expect something.

Probably - means that if current token has given type - it goes to next token and returns True,
    otherwise - returnes False.
Expect - means that if current token has given type - it goes to next token and returns True,
    otherwise - raises Exception
Is type - means that if current token has given type - returns True, otherwise - False.
Line is - means if line has given type - returns True, otherwise - False.
    Assume, that current token - is first token in line.
Get - means if token has given type - returns it's value, otherwise - raises error.
Detect line - detects type of given line, returns it.

All this functions will be assigned to Parser class as methods,
use them as "self.method_name()", no need to import them.
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


def probably_comment(self):
    if self.current_token.name == 'COMMENT':
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
    if self.current_token.name in represent.EOL_TOKENS:
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
        self.raise_parse_error(expected=f'some EOL token: {represent.EOL_TOKENS}')


def expect_name(self):
    if self.probably_name():
        return True
    else:
        self.raise_expected_name()


def expect_comment(self):
    if self.probably_comment():
        return True
    else:
        self.raise_parse_error(expected='COMMENT token')


def expect_unary_operator(self):
    pass


def expect_binary_operator(self):
    pass


def line_is_comment(self):
    """Checks current and next tokens to detect: is it a comment, or not
    Often is used on a start of line to detect: does it containg
        comment, or expression, or statement
    """
    if self.current_token.name == 'COMMENT':
        return True
    else:
        return False


def line_is_statement(self):
    """Checks current and next tokens to detect: is it expression, or not
    Often is used on a start of line to detect: does it has expression or statement
    """
    if self.current_token.name in ['NAME', 'IMPORT', 'FROM',
        'FUNCTION', 'DEF', 'RETURN', 'YIELD', 'GLOBAL', 'NONLOCAL', 'ASYNC', 'AWAIT',
        'CLASS',
        'FOR', 'WHILE', 'IF', 'SWITCH',
        'TRY', 'RAISE', 'ASSERT', 'WITH', 'DEL',
    ]:
        # if there's only one name in line - it's returned and it's expression
        if self.current_token.name == 'NAME':
            cur_position = self.current_token_index
            self.next_token()
            if self.is_type('EOL'):
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
    """
    if self.current_token.name in (
        ['NAME', 'NUMBER', 'STRING', 'LPAR', 'FN'] + represent.UNARY_OPERATORS
    ):
        start_of_line = self.current_token_index
        end_of_line = self.find_end_of_expression_line()

        # detect "=" inside of line, they're marker that it's statement
        for indx in range(start_of_line, end_of_line + 1):
            if self.tokens[indx].name == 'EQUAL': return False

        return True
    else:
        return False


def line_is_empty(self):
    """Checks, whether line contains something, or not.
    """
    if self.current_token.name == 'EOL':
        return True
    else:
        return False


def is_type(self, token_type):
    """If current token has given type - returns True, otherwise - False.
    """
    if self.current_token.name == token_type:
        return True
    else:
        return False


def is_name(self):
    """If current token has type name, returns True, otherwise - False.
    """
    if self.current_token.name == 'NAME':
        return True
    else:
        return False


def is_eol(self):
    """If current token represents end of line - returns True, otherwise - False.
    """
    if self.current_token.name in represent.EOL_TOKENS:
        return True
    else:
        return False


def is_string_literal(self):
    # probably not needed because scanner returns token type string,
    # it's value - string value
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


def detect_line_type(self):
    """Wrapper over is_expression(), is_statement(), is_comment()
    Detects near data type (starting from current token)
    Often is used on a start of line to detect: does it has expression or statement
    It checks for statement first, because statement detection is more easy.
    Returns:
        'comment', 'statement', 'expression'
    """
    if self.line_is_empty():
        return 'empty'
    elif self.line_is_comment():
        return 'comment'
    elif self.line_is_statement():
        return 'statement'
    elif self.line_is_expression():
        return 'expression'
    else:
        self.raise_unknown_line()
