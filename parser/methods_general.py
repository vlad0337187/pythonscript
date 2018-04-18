"""Contains general methods of Parser class for parsing source code.
"""


def skip_identifier(self):
    """Skips indetifier, returns token's name.
    """
    if self.current_token.name in [
        'IMPORT', 'FROM', 'AS',
        'FUNCTION', 'DEF', 'RETURN', 'YIELD', 'GLOBAL', 'NONLOCAL',
        'ASYNC', 'AWAIT',
        'CLASS',
        'FOR', 'WHILE', 'BREAK', 'CONTINUE',
        'IF', 'ELIF', 'ELSE',
        'SWITCH', 'WHEN',
        'TRY', 'EXCEPT', 'FINALLY', 'RAISE', 'ASSERT',
        'WITH',
        'IS', 'NOT', 'OR', 'AND', 'IN', 'DELETE',
    ]:
        name = self.current_token.name
        self.next_token()
        return name


def get_name_with_dots(self):
    """Returns string of such type: 'name.name2', or just 'name'
    Wrapper over get_names_divided_by_dots()
    """
    name = self.get_names_divided_by_dots()
    if len(name) > 1:  # convert to such string: 'os.path.dirname'
        name = '.'.join(name)
    else:
        name = name[0]
    return name


def get_names_divided_by_dots(self):
    """Returns list of strings, which were divided by dots
    Like this: 'name_1.name_2'
    """
    attributes = []
    while True:
        attr = self.get_name()
        attributes.append(attr)
        if self.probably('DOT'):
            continue
        break
    return attributes


def count_amount_of_dots(self):
    dots_amount = 0
    while True:
        if self.probably('DOT'):
            dots_amount += 1
            continue
        elif self.probably('ELLIPSIS'):  # it's made from dots too
            dots_amount += 3
            continue
        else:
            break
    return dots_amount
