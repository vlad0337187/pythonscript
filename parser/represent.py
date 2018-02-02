"""Describes what do tokens represent.
"""


ALL_OPERATORS = [
    # contains all tokens, that are operators
    # doesn't includes assingments
    'OPERATOR',
    'IS',
    'NOT',
    'OR',
    'IN',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'DOUBLESLASH',
    'PERCENT',
    'VBAR',
    'AMPER',
    'LESS',
    'GREATER',
    'TILDE',
    'CIRCUMFLEX',
    'LEFTSHIFT',
    'RIGHTSHIFT',
    'DOUBLESTAR',
    'EQEQUAL',
    'NOTEQUAL',
    'LESSEQUAL',
    'GREATEREQUAL',
]


UNARY_OPERATORS = ['PLUS', 'MINUS', 'NOT', ]
LITERALS = ['STRING', 'NUMBER', ]


OPERATORS_PRIORITY = {
    # - most of operators' names were taken from 'TOKEN_DICT' from tokenlist.py
    # - to check priority: OPERATORS_PRIORITY[operator]
    # - ATTENTION:
    #       - unary '+' and unary '-' are marked as 'UPLUS' and 'UMINUS'
    #       - there is no such token 'IS NOT', it's just operator,
    #         same for 'NOT IN'
    # - Not paying attention that line, containing assignment operator,
    #       is statement;
    #       line, containing all other operators is expression (returns value),
    #       all operators are listed here, because this dict describes priority.
    'DOUBLESTAR': 130,         # '**' - raising to power

    'TILDE': 120,              # '~'  - complement operator, flips bits
    'UPLUS': 120,              # '+'  - unary plus
    'UMINUS': 120,             # '-'  - unary minus

    'STAR': 110,               # '*'  - multiply
    'SLASH': 110,              # '/'  - divide
    'DOUBLESLASH': 110,        # '//' - floor division
    'PERCENT': 110,            # '%'  - get remainder after division

    'PLUS': 100,               # '+'  - addition
    'MINUS': 100,              # '-'  - subtraction

    'LEFTSHIFT': 90,           # '<<' - left bitwise shift
    'RIGHTSHIFT': 90,          # '>>' - right bitwise shift

    'AMPER': 80,               # '&'  - bitwise and

    'CIRCUMFLEX': 70,          # '^'  - bitwise inclusive or
    'VBAR': 70,                # '|'  - regular or

    'LESS': 60,                # '<'  - lesser
    'GREATER': 60,             # '>'  - greater
    'LESSEQUAL': 60,           # '<=' - lesser or equal
    'GREATEREQUAL': 60,        # '>=' - greater or equal

    'EQEQUAL': 50,             # '==' - equal
    'NOTEQUAL': 50,            # '!=' - not equal

    'EQUAL': 40,               # '='   - assign
    'PLUSEQUAL': 40,           # '+='  - add and assign
    'MINUSEQUAL': 40,          # '-='  - subtract and assign
    'STAREQUAL': 40,           # '*='  - multiply and assign
    'SLASHEQUAL': 40,          # '/='  - divide and assign
    'PERCENTEQUAL': 40,        # '%='  - get remainder after division and assign
    'AMPEREQUAL': 40,          # '&='  - bitwise "and" and assign
    'VBAREQUAL': 40,           # '|='  - regular "or" and assign
    'CIRCUMFLEXEQUAL': 40,     # '^='  - bitwise inclusive "or" and assign
    'LEFTSHIFTEQUAL': 40,      # '<<=' - left bitwise shift and assign
    'RIGHTSHIFTEQUAL': 40,     # '>>=' - right bitwise shift and assign
    'DOUBLESTAREQUAL': 40,     # '**=' - raise to power and assign
    'DOUBLESLASHEQUAL': 40,    # '//=' - floor division and assign
    'ATEQUAL': 40,             # '@='  - don't really know what it does, maybe to remove it

    'IS': 30,                  # 'is'     - checks identity of objects
    'IS NOT': 30,              # 'is not' - checks that objects are not same

    'IN': 20,                  # 'in'     - membership check
    'NOT IN': 20,              # 'not in' - non-membership check

    'NOT': 10,                 # 'not' - unary logical not
    'AND': 10,                 # 'and' - logical and
    'OR': 10,                  # 'or'  - logical or
}


OPERATORS_DIRECTION = {
    # direction, on which to apply operators if they have same priority
}


EOL_TOKENS = [
    # tokens, that represent end of general line with source code - end of expression
    'SEMICOLON', 'EOL',
]
