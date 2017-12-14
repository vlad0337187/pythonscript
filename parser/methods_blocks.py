"""Contains methods for parsing blocks \ lines, etc.
"""


def parse_block(self):
    """Parses block, returns AST node.
    Block - is, for example, body of function, or of class, or of module.
    Returns list of nodes.
    """
    block_nodes = []
    while True:
        line = self.parse_line()
        print('this time "line" was:', line)
        if line == 'EOL':
            continue
        elif line == 'EOF':
            break
        elif line == 'COMMENT':
            continue
        elif line:  # some AST node
            block_nodes.append(line)
        else:
            self.raise_parse_error(expected=('statement', 'expression', 'comment', 'EOL', 'EOF'))

    return block_nodes


def parse_line(self):
    """Parses one line.
    Doesn't matter, is it real line, or inline line,
    or line was continued. Parses all till the logic end of line.
    If line was not started - searches it's start and parses it.\
    Returns AST node which was on current line; False if line contained comment,
    or None if it was a comment.
    """
    node = None

    if self.current_token.name == 'EOL':
        self.next_token()
        node = 'EOL'
    elif self.current_token.name == 'EOF':
        node = 'EOF'
    elif self.line_is_comment():  # add accept_comment
        node = 'COMMENT'
    elif self.line_is_statement():
        node = self.parse_statement()
    elif self.line_is_expression():
        #node = self.parse_expression()  # will be uncomented later
        raise ValueError('expressions are unsupported yet')
    else:
        self.raise_parse_error(expected=('statement', 'expression', 'comment'))

    if not node:
        raise ValueError('node was None')
    return node
