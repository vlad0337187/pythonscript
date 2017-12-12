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
