"""
Contains list of tokens, token classes and things to operate with them.
"""


# list of all tokens:


TOKEN_DICT = {
    # 59 items,   46 were from standard detail tokens
    'EOF': {'token_id': 0},  # EOF
    #'NL': {'token_id': 1},  # maybe to remove this. Were similar: NEWLINE, NL
    'NAME': {'token_id': 2},  # all stuff, like variable's names, some operators
    'OPERATOR': {'token_id': 3},  # other operator, except specified below
    'NUMBER': {'token_id': 4},  # all kinds of numbers (integer: 1, 2; floats: 0.5, 2.8, octal: 0o100, hexadecimal:0x40, little: 0e2)
    'STRING': {'token_id': 5},
    'EOL': {'token_id': 6},  # end of line
    'INDENT': {'token_id': 7},  # tabs amount from starting of line increased
    'DEDENT': {'token_id': 8},  # tabs amount from starting of line decreased
    'COMMENT': {'token_id': 9, 'string_repr': '#'},

    'ERRORTOKEN': {'token_id': 20},
    'N_TOKENS': {'token_id': 21},
    'NT_OFFSET': {'token_id': 22},  # Special definitions for cooperation with parser
    # (shows current offset (tabs or spaces amount))

    'IMPORT': {'token_id': 40, 'string_repr': 'import'},  # import statement
    # 'USING': {'token_id': 41, 'string_repr': 'using'},  # maybe to remove it, but implicitly import this function
    'FROM': {'token_id': 42, 'string_repr': 'from'},
    'AS': {'token_id': 43, 'string_repr': 'as'},

    'FUNC': {'token_id': 50, 'string_repr': 'function'},
    'RETURN': {'token_id': 52, 'string_repr': 'return'},
    'YIELD': {'token_id': 33, 'string_repr': 'yield'},
    'GLOBAL': {'token_id': 34, 'string_repr': 'global'},
    'NONLOCAL': {'token_id': 35, 'string_repr': 'nonlocal'},

    'AWAIT': {'token_id': 60, 'string_repr': 'await'},
    'ASYNC': {'token_id': 61, 'string_repr': 'async'},

    'CLASS': {'token_id': 70, 'string_repr': 'class'},

    'FOR': {'token_id': 80, 'string_repr': 'for'},
    'WHILE': {'token_id': 81, 'string_repr': 'while'},
    'BREAK': {'token_id': 82, 'string_repr': 'break'},
    'CONTINUE': {'token_id': 83, 'string_repr': 'continue'},

    'IF': {'token_id': 90, 'string_repr': 'if'},
    'ELIF': {'token_id': 91, 'string_repr': 'elif'},
    'ELSE': {'token_id': 92, 'string_repr': 'else'},

    'SWITCH': {'token_id': 100, 'string_repr': 'switch'},
    'WHEN': {'token_id': 101, 'string_repr': 'when'},

    'TRY': {'token_id': 110, 'string_repr': 'try'},
    'EXCEPT': {'token_id': 111, 'string_repr': 'except'},
    'FINALLY': {'token_id': 112, 'string_repr': 'finally'},
    'RAISE': {'token_id': 113, 'string_repr': 'raise'},
    'ASSERT': {'token_id': 114, 'string_repr': 'assert'},

    'WITH': {'token_id': 116, 'string_repr': 'with'},

    'IS': {'token_id': 120, 'string_repr': 'is'},
    'NOT': {'token_id': 121, 'string_repr': 'not'},
    'AND': {'token_id': 122, 'string_repr': 'and'},
    'OR': {'token_id': 123, 'string_repr': 'or'},
    'IN': {'token_id': 124, 'string_repr': 'in'},
    'DELETE': {'token_id': 125, 'string_repr': 'delete'},

    'LPAR': {'token_id': 130, 'string_repr': '('},
    'RPAR': {'token_id': 131, 'string_repr': ')'},
    'LSQB': {'token_id': 132, 'string_repr': '['},
    'RSQB': {'token_id': 133, 'string_repr': ']'},
    'LBRACE': {'token_id': 134, 'string_repr': '{'},
    'RBRACE': {'token_id': 135, 'string_repr': '}'},

    'COLON': {'token_id': 140, 'string_repr': ':'},
    'COMMA': {'token_id': 141, 'string_repr': ','},
    'SEMICOLON': {'token_id': 142, 'string_repr': ';'},
    'DOT': {'token_id': 143, 'string_repr': '.'},
    'AT': {'token_id': 144, 'string_repr': '@'},
    'RARROW': {'token_id': 146, 'string_repr': '->'},
    'LARROW': {'token_id': 147, 'string_repr': '<-'},
    'ELLIPSIS': {'token_id': 148, 'string_repr': '...'},

    'PLUS': {'token_id': 160, 'string_repr': '+'},
    'MINUS': {'token_id': 161, 'string_repr': '-'},
    'STAR': {'token_id': 162, 'string_repr': '*'},
    'SLASH': {'token_id': 163, 'string_repr': '/'},
    'DOUBLESLASH': {'token_id': 164, 'string_repr': '//'},
    'PERCENT': {'token_id': 165, 'string_repr': '%'},
    'VBAR': {'token_id': 166, 'string_repr': '|'},
    'AMPER': {'token_id': 167, 'string_repr': '&'},
    'LESS': {'token_id': 168, 'string_repr': '<'},
    'GREATER': {'token_id': 169, 'string_repr': '>'},
    'TILDE': {'token_id': 170, 'string_repr': '~'},  # complement operator, flips bits
    'CIRCUMFLEX': {'token_id': 171, 'string_repr': '^'},
    'LEFTSHIFT': {'token_id': 172, 'string_repr': '<<'},
    'RIGHTSHIFT': {'token_id': 173, 'string_repr': '>>'},
    'DOUBLESTAR': {'token_id': 174, 'string_repr': '**'},

    'EQEQUAL': {'token_id': 190, 'string_repr': '=='},
    'NOTEQUAL': {'token_id': 191, 'string_repr': '!='},
    'LESSEQUAL': {'token_id': 192, 'string_repr': '<='},
    'GREATEREQUAL': {'token_id': 193, 'string_repr': '>='},

    'EQUAL': {'token_id': 194, 'string_repr': '='},
    'PLUSEQUAL': {'token_id': 195, 'string_repr': '+='},
    'MINUSEQUAL': {'token_id': 196, 'string_repr': '-='},
    'STAREQUAL': {'token_id': 197, 'string_repr': '*='},
    'SLASHEQUAL': {'token_id': 198, 'string_repr': '/='},
    'PERCENTEQUAL': {'token_id': 199, 'string_repr': '%='},
    'AMPEREQUAL': {'token_id': 200, 'string_repr': '&='},
    'VBAREQUAL': {'token_id': 201, 'string_repr': '|='},
    'CIRCUMFLEXEQUAL': {'token_id': 202, 'string_repr': '^='},
    'LEFTSHIFTEQUAL': {'token_id': 203, 'string_repr': '<<='},
    'RIGHTSHIFTEQUAL': {'token_id': 204, 'string_repr': '>>='},
    'DOUBLESTAREQUAL': {'token_id': 205, 'string_repr': '**='},
    'DOUBLESLASHEQUAL': {'token_id': 206, 'string_repr': '//='},
    'ATEQUAL': {'token_id': 207, 'string_repr': '@='},
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

    def show_details(self):
        """Returns string with detailed description of token.
        """
        return f'''Token:
Name: {self.name}
Text: {self.text}
Starts (line number, character number): {self.starts}
Ends (line number, character number): {self.ends}'''

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
