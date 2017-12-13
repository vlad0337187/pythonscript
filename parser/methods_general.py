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
        'IS', 'NOT', 'OR', 'AND', 'IN', 'DEL',
    ]:
        name = self.current_token.name
        self.next_token()
        return name
