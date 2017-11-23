"""
Contains list of tokens, token classes and things to operate with them.
"""


# list of all tokens:


TOKEN_DICT = {
    # 59 items,   46 were from standard detail tokens
    'ENDMARKER' = {'int': 0},  # EOF
    'NAME' = {'int': 1},  # all stuff, like variable's names, some operators
    'NUMBER' = {'int': 2},
    'STRING' = {'int': 3},
    'NEWLINE' = {'int': 4},
    'INDENT' = {'int': 5},
    'DEDENT' = {'int': 6},
    'LPAR' = {'int': 7, 'string': '('},
    'RPAR' = {'int': 8, 'string': ')'},
    'LSQB' = {'int': 9, 'string': '['},
    'RSQB' = {'int': 10, 'string': ']'},
    'COLON' = {'int': 11, 'string': ':'},
    'COMMA' = {'int': 12, 'string': ','},
    'SEMI' = {'int': 13, 'string': ';'},
    'PLUS' = {'int': 14, 'string': '+'},
    'MINUS' = {'int': 15, 'string': '-'},
    'STAR' = {'int': 16, 'string': '*'},
    'SLASH' = {'int': 17, 'string': '/'},
    'VBAR' = {'int': 18, 'string': '|'},
    'AMPER' = {'int': 19, 'string': '&'},
    'LESS' = {'int': 20, 'string': '<'},
    'GREATER' = {'int': 21, 'string': '>'},
    'EQUAL' = {'int': 22, 'string': '='},
    'DOT' = {'int': 23, 'string': '.'},
    'PERCENT' = {'int': 24, 'string': '%'},
    'LBRACE' = {'int': 25, 'string': '{'},
    'RBRACE' = {'int': 26, 'string': '}'},
    'EQEQUAL' = {'int': 27, 'string': '=='},
    'NOTEQUAL' = {'int': 28, 'string': '!='},
    'LESSEQUAL' = {'int': 29, 'string': '<='},
    'GREATEREQUAL' = {'int': 30, 'string': '>='},
    'TILDE' = {'int': 31, 'string': '~'},
    'CIRCUMFLEX' = {'int': 32, 'string': '^'},
    'LEFTSHIFT' = {'int': 33, 'string': '<<'},
    'RIGHTSHIFT' = {'int': 34, 'string': '>>'},
    'DOUBLESTAR' = {'int': 35, 'string': '**'},
    'PLUSEQUAL' = {'int': 36, 'string': '+='},
    'MINEQUAL' = {'int': 37, 'string': '-='},
    'STAREQUAL' = {'int': 38, 'string': '*='},
    'SLASHEQUAL' = {'int': 39, 'string': '/='},
    'PERCENTEQUAL' = {'int': 40, 'string': '%='},
    'AMPEREQUAL' = {'int': 41, 'string': '&='},
    'VBAREQUAL' = {'int': 42, 'string': '|='},
    'CIRCUMFLEXEQUAL' = {'int': 43, 'string': '^='},
    'LEFTSHIFTEQUAL' = {'int': 44, 'string': '<<='},
    'RIGHTSHIFTEQUAL' = {'int': 45, 'string': '>>='},
    'DOUBLESTAREQUAL' = {'int': 46, 'string': '**='},
    'DOUBLESLASH' = {'int': 47, 'string': '//'},
    'DOUBLESLASHEQUAL' = {'int': 48, 'string': '//='},
    'AT' = {'int': 49, 'string': '@'},
    'ATEQUAL' = {'int': 50, 'string': '@='},
    'RARROW' = {'int': 51, 'string': '->'},
    'ELLIPSIS' = {'int': 52, 'string': '...'},
    'OP' = {'int': 53},
    'AWAIT' = {'int': 54, 'string': 'await'},  # added string
    'ASYNC' = {'int': 55, 'string': 'async'},  # added string
    'ERRORTOKEN' = {'int': 56},
    'N_TOKENS' = {'int': 57},
    'NL' = {'int': 58},
    'NT_OFFSET' = {'int': 256},  # Special definitions for cooperation with parser
    # shows current offset (tabs or spaces amount)
}


class Token:
    name = ''  # corresponds to name in TOKEN_DICT.keys()
    integer = None  # corresponds TOKEN_DICT['name']['int']
    string = ''  # corresponds TOKEN_DICT['name']['string']
    value = ''  # real value from source code (line or string)
    starts = ('', '') # (row, column) indices of the token (a 2-tuple of ints)
    ends = ('', '') # (row, column) indices of the token (a 2-tuple of ints)

    def is_terminal(self):  # figure out
        return self < NT_OFFSET

    def is_not_terminal(self):
        return self >= NT_OFFSET

    def is_eof(self):
        '''
        Shows whether this token is EOF token.
        '''
        return x == ENDMARKER



# Old stuff:   (may be removed later)


# Represents predefined tokens.
#    Name of token - it's string representation.
#    Id - unique number of every token.
#    Structure: NAME = id
#    This is a static class (no need in instance creation).

TOKEN_ENUM = {  # copied from standart Python's tokenizer.py
    # may be removed later if not needed
    'ENDMARKER': 0,  # 59 items
    'NAME': 1,
    'NUMBER': 2,
    'STRING': 3,
    'NEWLINE': 4,
    'INDENT': 5,
    'DEDENT': 6,
    'LPAR': 7,
    'RPAR': 8,
    'LSQB': 9,
    'RSQB': 10,
    'COLON': 11,
    'COMMA': 12,
    'SEMI': 13,
    'PLUS': 14,
    'MINUS': 15,
    'STAR': 16,
    'SLASH': 17,
    'VBAR': 18,
    'AMPER': 19,
    'LESS': 20,
    'GREATER': 21,
    'EQUAL': 22,
    'DOT': 23,
    'PERCENT': 24,
    'LBRACE': 25,
    'RBRACE': 26,
    'EQEQUAL': 27,
    'NOTEQUAL': 28,
    'LESSEQUAL': 29,
    'GREATEREQUAL': 30,
    'TILDE': 31,
    'CIRCUMFLEX': 32,
    'LEFTSHIFT': 33,
    'RIGHTSHIFT': 34,
    'DOUBLESTAR': 35,
    'PLUSEQUAL': 36,
    'MINEQUAL': 37,
    'STAREQUAL': 38,
    'SLASHEQUAL': 39,
    'PERCENTEQUAL': 40,
    'AMPEREQUAL': 41,
    'VBAREQUAL': 42,
    'CIRCUMFLEXEQUAL': 43,
    'LEFTSHIFTEQUAL': 44,
    'RIGHTSHIFTEQUAL': 45,
    'DOUBLESTAREQUAL': 46,
    'DOUBLESLASH': 47,
    'DOUBLESLASHEQUAL': 48,
    'AT': 49,
    'ATEQUAL': 50,
    'RARROW': 51,
    'ELLIPSIS': 52,
    'OP': 53,
    'AWAIT': 54,
    'ASYNC': 55,
    'ERRORTOKEN': 56,
    'N_TOKENS': 57,
    'NT_OFFSET': 256,
}


# Defines matching of token's unique numbers (values of TokenEnum) and
# actual symbols for that tokens.

EXACT_TOKEN_TYPES = {  # 46 items
    '(':   TOKEN_ENUM['LPAR'],
    ')':   TOKEN_ENUM['RPAR'],
    '[':   TOKEN_ENUM['LSQB'],
    ']':   TOKEN_ENUM['RSQB'],
    ':':   TOKEN_ENUM['COLON'],
    ',':   TOKEN_ENUM['COMMA'],
    ';':   TOKEN_ENUM['SEMI'],
    '+':   TOKEN_ENUM['PLUS'],
    '-':   TOKEN_ENUM['MINUS'],
    '*':   TOKEN_ENUM['STAR'],
    '/':   TOKEN_ENUM['SLASH'],
    '|':   TOKEN_ENUM['VBAR'],
    '&':   TOKEN_ENUM['AMPER'],
    '<':   TOKEN_ENUM['LESS'],
    '>':   TOKEN_ENUM['GREATER'],
    '=':   TOKEN_ENUM['EQUAL'],
    '.':   TOKEN_ENUM['DOT'],
    '%':   TOKEN_ENUM['PERCENT'],
    '{':   TOKEN_ENUM['LBRACE'],
    '}':   TOKEN_ENUM['RBRACE'],
    '==':  TOKEN_ENUM['EQEQUAL'],
    '!=':  TOKEN_ENUM['NOTEQUAL'],
    '<=':  TOKEN_ENUM['LESSEQUAL'],
    '>=':  TOKEN_ENUM['GREATEREQUAL'],
    '~':   TOKEN_ENUM['TILDE'],
    '^':   TOKEN_ENUM['CIRCUMFLEX'],
    '<<':  TOKEN_ENUM['LEFTSHIFT'],
    '>>':  TOKEN_ENUM['RIGHTSHIFT'],
    '**':  TOKEN_ENUM['DOUBLESTAR'],
    '+=':  TOKEN_ENUM['PLUSEQUAL'],
    '-=':  TOKEN_ENUM['MINEQUAL'],
    '*=':  TOKEN_ENUM['STAREQUAL'],
    '/=':  TOKEN_ENUM['SLASHEQUAL'],
    '%=':  TOKEN_ENUM['PERCENTEQUAL'],
    '&=':  TOKEN_ENUM['AMPEREQUAL'],
    '|=':  TOKEN_ENUM['VBAREQUAL'],
    '^=':  TOKEN_ENUM['CIRCUMFLEXEQUAL'],
    '<<=': TOKEN_ENUM['LEFTSHIFTEQUAL'],
    '>>=': TOKEN_ENUM['RIGHTSHIFTEQUAL'],
    '**=': TOKEN_ENUM['DOUBLESTAREQUAL'],
    '//':  TOKEN_ENUM['DOUBLESLASH'],
    '//=': TOKEN_ENUM['DOUBLESLASHEQUAL'],
    '...': TOKEN_ENUM['ELLIPSIS'],
    '->':  TOKEN_ENUM['RARROW'],
    '@':   TOKEN_ENUM['AT'],
    '@=':  TOKEN_ENUM['ATEQUAL'],
}
