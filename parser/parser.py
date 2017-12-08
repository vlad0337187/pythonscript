import navigation_methods
import expecting_methods


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0  # index of current token
        self.last_token_index = len(tokens) - 1
        self.current_token = tokens[0]

    def parse(self):
        """Parses self.tokens to AST tree, returns it.
        """

    def parse_expression(self):
        pass

    def parse_inline_line(self):
        pass

    Parser.next_token = navigation_methods.next_token
    Parser.previous_token = navigation_methods.previous_token
    Parser.set_current_token = navigation_methods.set_current_token
