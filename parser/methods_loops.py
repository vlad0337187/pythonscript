"""Contains all for parsing loops.
"""


def parse_for_statement(self):
    """Parses such syntax: 'for x in a ->   c = x + b'
    """
    pass


def parse_for_expression(self):
    """Parses such syntax: 'a = for x in b ->   b + 4'
    This expression returns tuple, made from last line on every iteration.
    """
    pass


def parse_while_statement(self):
    """Parses such syntax: 'while x < 4 ->   c.append(x + b);   x += 4'
    """
    pass


def parse_while_expression(self):
    """Parses such syntax: 'a = while x < 4 ->   x += 1;   4 + x'
    """
    pass
