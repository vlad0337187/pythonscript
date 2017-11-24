Main details:
- It's a little language, which can be used with CPython interpreter.
- It's launched by importing to .py file from .python file using "using" function of pythonscript module.
    Examples:
    - general import (in .py file):
        ```python
        from pythonscript import using
        using("modulename")

        modulename.function_name('some argument')
        ```
        using() searches for PythonScript modules and packages just like Python's "import" statement does,
        after compiles them to AST (using Python's "ast" module), creates module object from it and adds it to
        sys.modules list.
        After this you can use it just like general Python module.
    - importing only specified attributes:
        ```python
        using_from("modulename", "attribute_1", "attr_2")

        some_var = 485 + attr_2
        ```
    - importing with imitation of Python's "as" operator:
        ```python
        using({"some_long_modulename": "alias_1"}, {"long_modulename_2": "al_2"})

        alias_1.function_1()
        al_2.function_2()
        ```
    - importing just like "from mname import attrname as attr"
        ```python
        using_from("module_name", {"attribute_to_rename": "alias"})
        ```
- It can use Python's modules just like it's own.
    Examples:
    - in PythonScript source file: (syntax is the same)
        ```python
        import python_module as pm
        from python_module_2 import attr_1 as at
        ```
- It has equal to Python running speed.
    - It only takes more time to compile at first time (because parser / compiler is written in Python),
    after this it works with same speed just like regular Python module.
    - After it was compiled first time, it saves bytecode to \__pythoncache__ folder, and all next
        imports will be done with same to Python speed.




Main goals (by order):
- Elegance:
    - clear syntax, not overdosed with symbols,
        better using real words
    - Similarity to Python, CoffeeScript code
- Usability:
    - almost all may could be combined as user wishes
    - programmer chooses style of code by his own
        (would it be code with brackets, or with indents, or all would be written into one line)
        ```coffeescript
        # Is valid:
        if (a == 4) {
            b = 8;
            c = 9;
        }
        # Such is valid too:
        if a == 4
            b = 8
            c = 9
        ```
    - all code could be written in one line, or could be written in
        separate lines, depends on what developer think
    - often-used tasks may be written with more clear syntax than lesser-used ones.
- Just Python:
    - it must be just Python, nothing more or less
    - 100% compatibility with CPython implementation, maximum - with others.




Scopes and brackets:
- PythonScript uses line-based scoping.
    - One expression must be on one line. But lines can be emulated by brackets "()" (all inside
    such brackets is considered as one line). Also line end can be emulated with ";", after it new
    line starts.
    WIth "->" we can emulate indent (EOL + indent, there is no separate token for indent
    because indent cannot be without new line),
    with "<-" - dedent (EOL + dedent).

    - "{}" are ignored (you can place them where you want, used for visual purposes.
        (except inside strings))
    "()" are used for grouping. All inside of them can be considered as one line or one group.
    "[]" are using for taking arguments and slices
- About "()":
    - if line starts with "(", it will not be finished until ")"
    even dedent is ignored, not talking about "<-" or ";"
    - also this line can be considered as "inline line", because
        "(" in the center of line will not be considered as end of current line;
        but starting new one (what ";") will be considered like line in other line.
    - If new inline line (using "()") was met in center of general line (or other inline line),
        it must contain expression (must return something),
    - And if "(" was on the start of real line (after indent if it was, of course),
        than it could have also statements
        (and it still will not be finished until ")")
    - If "(" was met just after statement keywords (which support it)
    - If "(" was met just after function name, it's considered that started by it "inline" line contains
        passed to function arguments (separated with commas).
        ```coffeescript
        function_name(arg_1, arg_2, *args, **kwargs)
        ```
        - If it's empty, it's considered as passing to function zero arguments.
            If function name was alone in one line - line will just return that function object.
            ```coffeescript
            function_1()  # will be launched
            function_2  # wil return function_2 object
            ```
    - If "(" was met after separator (space) after function name, it's considered that started line for defining
        first function's argument (and "inline" line must contain expression (return something)).
        ```coffeescript
        function_name (4 + 8), arg_2, (3 + arg_3)
        ```




# Collections types:
- #### Literals:
    - ##### Lists:
        ```coffeescript
        list 1, 2, 3, 4, 5, 6
        list 1, 2, 3, def a, b -> return a + b <-, 4, 5, 6
        list 1, 2, 3, (def a, b -> return a + b), 4, 5, 6
        ```
        - multiline list definition using block syntax (will be readed until dedent):
            ```coffeescript
            list
                1, 2, 3,
                4, 5, 6
            # block - is all that spans after block keyword + indent until dedent
            ```
        - using brackets:
            ```coffeescript
                (list 1, 2, 3
            4, 5, 6)
                # if line starts with "(", it will not be finished until ")"
                # even dedent is ignored, not talking about "<-" or ";"
                # also this line can be considered as "inline line", because
            ```
    - ##### Sets:
        ```coffeescript
        set 1, 2, 10, 'a'
        ```
    - ##### Dicts:
        ```coffeescript
        dict  1: 4,  5: b,  'new_value': 344
        dict
            1: 4,         2: 'string',   3: 8;
            var_1: 224,   var_2: 348,    9: 6
            'a': 15,      'b': 18,       c: 21
        dict 1: 4, 5: b, 8: c
        (dict  'a': 8,  22: 4,
            23: 'ab')
        ```
    - ##### Running methods on collections literals:
        ```coffeescript
        list 1, 2, 3, 4;  .reverse()  .some_method()

        set 1, 2, 3
        .union set_2

        (list 1, 2, 3, 4).reverse().some_method()
        ```
- #### Taking by index:
    - ##### Lists:
        ```coffeescript
        a = list 1, 2, 3, 4
        a[1]  # will give 1
        a [2]  # will give 2
        a [-1]  # will give 4
        a[-2]  # will give 3
        ```
    - ##### Tuples:
        are taking analogically to Lists
    - ##### Sets, Dicts:
        they doesn't support such operations

- #### Taking by key:
    - ##### Dicts:
        ```coffeescript
        a = dict 'a': 'b',  2: 3
        a['a']  # will give 'b'
        a [2]  # will give 3
        ```
    - ##### Lists, Tuples, Sets:
        doesn't support

- #### Taking slices:
    - ##### Lists:  (maybe change it and make ignoring all between [] for type hinting
        ```coffeescript
        a = list 1, 2, 3, 4, 'a'
        a[1..3]  # will give l[1, 2, 3]
        a [2 .. -2]  # will give l[2, 3, 4]
        a [1..-1 .. 2]  # will give l[1, 3, 'a']
        ```
    - ##### Tuples:
        analogically to Lists.
    - ##### Sets, Dictionaries:
        they doesn't support taking slices




# Generators:
- #### List generators:
    ```coffeescript
    gen list x for x in somevariable
    gen list x for x in list 1, 2, 3 <- if x != 2
    # for clarity you can do so (this has the same result)
    get list x for x in list -> 1, 2, 3 <- if x != 2
    # ("->" just makes block list definition, than finishes it with "<-"
    gen list i + 2 for i, v in (gen list i2 for i2 in range 4, 2)
    ```
- #### Tuple generators:
    same as list ones
- #### Dictionaries generators:
    ```coffeescript
    gen dict k: v for k, v in zip var_1, var_2
    gen dict k: v for k, v in (zip var_1, var_2)
    gen dict   k: v   for k, v   in   zip var_1, var_2
    gen dict k: v for k, v in (zip var_1, var_2) if k > v
    gen dict   k: v   for k, v   in (zip var_1, var_2)   if k > v
    ```




# Error handling (Try/Except):
- ##### Examples:
    ```coffeescript
        try
               expression
        except Exception
               expression
        finally
               expression

        try
               expression
        except Exception as inst
               expression
        finally
               expression

        try -> expression; expression_2
        except Exception: expression
        finally
               expression

        try -> expression; expression_2; except Exception as inst -> expression <- finally -> expression
    ```




# Functions:
- #### Definition:
    There are 2 variants of functions definitions:
    - statement (defines function, it's name):
        ```coffeescript
        function func_name arg_1, arg_2
            body
        ```
    - expression (returns function object, which can be assigned to variable,
        or passed as argument to other function, or to be a part of list definition, etc)
        ```coffeescript
        func_name = def arg_1, *args -> return args.append(arg_1)    # assigned to variable
        func_name def -> return 4   # passed as argument
        ```
- ##### Examples:
    ```coffeescript
    function name arg1, arg2, **kwargs
        expression
        expression2

    function name arg1, arg2, **kwargs -> expression; expression2

    name = def arg1, arg2 -> expression

    name = def arg1, arg2, **kwargs
            expression

    name = def arg1, arg2 -> expression

    def name argument -> expression; expression_2

    a = def *args, **kwargs -> expression
    ```

- ##### Wrong / correct examples:
    - wrong:
        ```coffeescript
        a = def (arg, args)    # because def waits for passing arguments, and here
                expression     # data in brackets does not return anything
        ```
    - correct:
        ```coffeescript
        a = def (arg), (arg + something)
            expression

        # also correct:
        a = def(arg, (arg + something)) -> expression
        ```
- #### Running functions:
    ```coffeescript
    a = def -> return 4
    a do    # will run function without arguments
    do a    # wrong syntax
        printer = def *args -> print args
    printer(arg_1, arg_2)
    printer arg_1, arg_2
    printer (arg_1, arg_2)    # wrong syntax. Expects argument, so "()" must return object or something
    ```




decorators
    Syntax is just like in python:
        ```
        @some_decorator
        a = def c, d -> return c + d

        @some_decorator; a = def c, d -> return c + d

        @some_decorator
        function calculate_difference var_1, var_2
            return var_2 - var_1
        ```




Inner implementation details:
       package consists of 3 main parts:
               tokens (list of all used in language tokens)
               scanner (scans souce code and creates list of found tokens (token stream))
               parser (scans list of found tokens (token stream), makes AST from it)
               modulule_creator (resulting AST packs into module, adds to sys.modules)
               package_finder
                       (finds .python files, packages (directories with `__init__.python`)
                       from sys.path directories)
               organizer
                       (after calling "uses()" function launches all other components by order)
       there would be no difference for compiler: in which line of something is,
               the only matter for containing token's lines is for showing user as debug
               info
