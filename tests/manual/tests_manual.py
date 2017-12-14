
import ast
a = """
import os
"""
a = ast.parse(a)
ast.dump(a)


import ast
a = """
from ....os import path
"""
a = ast.parse(a)
ast.dump(a)
