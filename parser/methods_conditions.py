"""Contains methods for parsing conditional statements / expressions.
"""


def parse_if_statement(self):
    """Parses such syntax: 'if a ->   a = 4'
    """
    pass


def parse_if_expression(self):
    """Parses such syntax: 'a = if b -> 3   <- elif c -> 4   <- else -> 5'
    This expression returns value on last line of first True condition.
    """
    pass


def parse_switch_statement(self):
    pass


def parse_switch_expression(self):
    pass
