"""Contains methods for parsing all connected with exceptions.
"""


def parse_try_statement(self):
    expect('TRY')
    expect_block_start()
    node_try_block = self.parse_block()
    expect('DEDENT')

    node_except_blocks = []
    node_else_block = None
    node_finally_block = None

    while accept('EXCEPT'):
        exception_name = self.get_name().text
        expect_block_start()
        node_except_block = self.parse_block()
        except_nodes.append(node_except_block)
    if accept('ELSE'):
        expect_block_start()
        node_except_block = self.parse_block()
    if accept('FINALY'):
        expect_block_start()
        node_finally_block = self.parse_block()


def parse_try_expression(self):
    pass


def parse_assert_expression(self):
    pass
