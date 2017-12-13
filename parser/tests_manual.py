"""Contains manual tests that will be pasted into Python console.
"""


import ast

a = ast.parse('''try:
    a = 4
except Exception:
    pass
''')

ast.dump(a)


output: "Module(body=[Try(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=4))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name=None, body=[Pass()])], orelse=[], finalbody=[])])"




import ast

a = ast.parse('''try:
    a = 4
except Exception:
    pass

18 + 2
''')

ast.dump(a)


output: "Module(body=[Try(body=[Assign(targets=[Name(id='a', ctx=Store())], value=Num(n=4))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name=None, body=[Pass()])], orelse=[], finalbody=[]), Expr(value=BinOp(left=Num(n=18), op=Add(), right=Num(n=2)))])"
