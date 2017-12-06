"""
Contains list of tokens, token classes and things to operate with them.
"""


# list of all tokens:


TOKEN_DICT = {
    # 59 items,   46 were from standard detail tokens
    'ENDMARKER': {'token_id': 0},  # EOF
    'NAME': {'token_id': 1},  # all stuff, like variable's names, some operators
    'NUMBER': {'token_id': 2},
    'STRING': {'token_id': 3},
    'NEWLINE': {'token_id': 4},
    'INDENT': {'token_id': 5},  # tabs amount from starting of line increased
    'DEDENT': {'token_id': 6},  # tabs amount from starting of line decreased
    'LPAR': {'token_id': 7, 'string_repr': '('},
    'RPAR': {'token_id': 8, 'string_repr': ')'},
    'LSQB': {'token_id': 9, 'string_repr': '['},
    'RSQB': {'token_id': 10, 'string_repr': ']'},
    'COLON': {'token_id': 11, 'string_repr': ':'},
    'COMMA': {'token_id': 12, 'string_repr': ','},
    'SEMI': {'token_id': 13, 'string_repr': ';'},
    'PLUS': {'token_id': 14, 'string_repr': '+'},
    'MINUS': {'token_id': 15, 'string_repr': '-'},
    'STAR': {'token_id': 16, 'string_repr': '*'},
    'SLASH': {'token_id': 17, 'string_repr': '/'},
    'VBAR': {'token_id': 18, 'string_repr': '|'},
    'AMPER': {'token_id': 19, 'string_repr': '&'},
    'LESS': {'token_id': 20, 'string_repr': '<'},
    'GREATER': {'token_id': 21, 'string_repr': '>'},
    'EQUAL': {'token_id': 22, 'string_repr': '='},
    'DOT': {'token_id': 23, 'string_repr': '.'},
    'PERCENT': {'token_id': 24, 'string_repr': '%'},
    'LBRACE': {'token_id': 25, 'string_repr': '{'},
    'RBRACE': {'token_id': 26, 'string_repr': '}'},
    'EQEQUAL': {'token_id': 27, 'string_repr': '=='},
    'NOTEQUAL': {'token_id': 28, 'string_repr': '!='},
    'LESSEQUAL': {'token_id': 29, 'string_repr': '<='},
    'GREATEREQUAL': {'token_id': 30, 'string_repr': '>='},
    'TILDE': {'token_id': 31, 'string_repr': '~'},
    'CIRCUMFLEX': {'token_id': 32, 'string_repr': '^'},
    'LEFTSHIFT': {'token_id': 33, 'string_repr': '<<'},
    'RIGHTSHIFT': {'token_id': 34, 'string_repr': '>>'},
    'DOUBLESTAR': {'token_id': 35, 'string_repr': '**'},
    'PLUSEQUAL': {'token_id': 36, 'string_repr': '+='},
    'MINEQUAL': {'token_id': 37, 'string_repr': '-='},
    'STAREQUAL': {'token_id': 38, 'string_repr': '*='},
    'SLASHEQUAL': {'token_id': 39, 'string_repr': '/='},
    'PERCENTEQUAL': {'token_id': 40, 'string_repr': '%='},
    'AMPEREQUAL': {'token_id': 41, 'string_repr': '&='},
    'VBAREQUAL': {'token_id': 42, 'string_repr': '|='},
    'CIRCUMFLEXEQUAL': {'token_id': 43, 'string_repr': '^='},
    'LEFTSHIFTEQUAL': {'token_id': 44, 'string_repr': '<<='},
    'RIGHTSHIFTEQUAL': {'token_id': 45, 'string_repr': '>>='},
    'DOUBLESTAREQUAL': {'token_id': 46, 'string_repr': '**='},
    'DOUBLESLASH': {'token_id': 47, 'string_repr': '//'},
    'DOUBLESLASHEQUAL': {'token_id': 48, 'string_repr': '//='},
    'AT': {'token_id': 49, 'string_repr': '@'},
    'ATEQUAL': {'token_id': 50, 'string_repr': '@='},
    'RARROW': {'token_id': 51, 'string_repr': '->'},
    'ELLIPSIS': {'token_id': 52, 'string_repr': '...'},
    'OP': {'token_id': 53},
    'AWAIT': {'token_id': 54, 'string_repr': 'await'},  # added string
    'ASYNC': {'token_id': 55, 'string_repr': 'async'},  # added string
    'ERRORTOKEN': {'token_id': 56},
    'N_TOKENS': {'token_id': 57},
    'NL': {'token_id': 58},
    'IMPORT': {'token_id': 59, 'string_repr': 'import'},  # import statement
    'NT_OFFSET': {'token_id': 256},  # Special definitions for cooperation with parser
    # shows current offset (tabs or spaces amount)
}


class Token:
    name = ''  # corresponds to name in TOKEN_DICT.keys()
    token_id = None  # corresponds TOKEN_DICT['name']['token_id']
    string_repr = ''  # corresponds TOKEN_DICT['name']['string_repr']
    text = ''  # real value from source code (line or string)
    context = ''  # line, where it was met. For debug info
    starts = (None, None) # data, about where token starts: (line_number, start_char_number)
    ends = (None, None) # data about where token ends: (line_number, start_char_number)

    def __init__(self, name=None, token_id=None, text='', starts=(None, None), ends=(None, None), context=''):
        if (not name) and (token_id):
            name = self.get_name_by_token_id(token_id)
        if (not token_id) and (name):
            token_id = self.get_token_id_by_name(name)

        self.name = name
        self.token_id = token_id
        self.text = text
        self.starts = starts
        self.ends = ends
        self.context = context

    @staticmethod
    def get_name_by_token_id(token_id):
        for token in TOKEN_DICT:
            if TOKEN_DICT[token]['token_id'] == token_id:
                return token

    @staticmethod
    def get_token_id_by_name(name):
        return TOKEN_DICT[name]['token_id']

    def is_terminal(self):  # figure out
        return self < NT_OFFSET

    def is_not_terminal(self):
        return self >= NT_OFFSET

    def is_eof(self):
        '''
        Shows whether this token is EOF token.
        '''
        return x == ENDMARKER
