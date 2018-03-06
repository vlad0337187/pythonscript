"""Contains methods for parsing blocks \ lines, etc.
Main file, it's methods are launched just after starting parsing with "parse.py".
"""


def parse_block(self, one_line=False):
    """Parses nodes to the end of block, returns list of AST nodes.
    Block - is, for example, body of function, or of class, or of module.
    Returns list of nodes.
    Arguments:
        mode: can be 'one' - that will be parsed only one line, can be None -
            will be parsed all block
    """
    block_nodes = []

    while True:
        node = None
        line_type = self.detect_line_type()

        if line_type == 'comment':
            self.expect_comment()
        elif line_type == 'statement':
            node = self.parse_statement()
        elif line_type == 'expression':
            node = self.parse_expression()
        elif line_type == 'empty':
            self.next_token()

        if one_line:
            return node
        if node:
            block_nodes.append(node)

    return block_nodes
