
# Main details:
- It's a little __programming language__, which can be used with CPython interpreter.
- It's launched by importing to .py file from .python file using "using" function of pythonscript module.
    __Examples:__
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
- It can use Python's __modules__ just like it's own.
    Examples:
    - in PythonScript source file: (syntax is the same)
        ```python
        import python_module as pm
        from python_module_2 import attr_1 as at
        ```
- It has equal to Python __running speed__.
    - It only takes more time to compile at first time (because parser / compiler is written in Python),
    after this it works with same speed just like regular Python module.
    - After it was compiled first time, it saves bytecode to \__pythoncache__ folder, and all next
        imports will be done with same to Python speed.




# Goals (by order):
- #### Giving pleasure from writing code because of:
    - ##### Elegance:
        - clear syntax, not overdosed with symbols,
            better using real words
        - Similarity to __Python__, __CoffeeScript__, __Genie__, __Nim__ code
    - ##### Usability:
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
    - ##### Just Python:
        - it must be just Python, nothing more or less
        - 100% compatibility with CPython implementation, maximum - with others. You may use any libraries and
            and frameworks that you want.




# Scopes and brackets:
- #### PythonScript uses "line-based" and "indent-based" scoping.
  - One expression must be on one line. But lines can be emulated by brackets "()" (all inside
   such brackets is considered as one line). Also line end can be emulated with ";", after it new
   line starts.
   WIth "->" we can emulate indent (EOL + indent, there is no separate token for indent
   because indent cannot be without new line),
   with "<-" - dedent (EOL + dedent).

  - __"{}"__ are ignored (you can place them where you want, used for visual purposes.
    (except inside strings))
  - __"()"__ are used for grouping. All inside of them can be considered as one line or one group.
  - __"[]"__ are using for taking arguments and slices
- #### About "()":
    - if line starts with __"("__, it will not be finished until __")"__
    even dedent is ignored, not talking about __"<-"__ or __";"__
    - also this line can be considered as _"inline line"_, because
        __"("__ in the center of line will not be considered as end of current line;
        but starting new one (what __";"__) will be considered like line in other line.
    - If new inline line (using __"()"__) was met in center of general line (or other inline line),
        it must contain expression (must return something),
    - And if __"("__ was on the start of real line (after indent if it was, of course),
        than it could have also statements
        (and it still will not be finished until __")"__)
    - If __"("__ was met just after statement keywords (which support it), than that statement considers
        all that "inline line" to belong it (and that line will not be finished until __")"__):
        ```coffeescript
        list(1, 3, 4
        4, 5, 6)
        # will create list, even "dedent" was ignored
        # (but this is a bad coding style example)
        ```
    - If __"("__ was met after statement keywords (which support it) after separator, than that "inline" line must give
        give some result, which statement will consider as it's argument:
        ````coffeescript
        list (4 + 8), 3, 4, 10
    - If __"("__ was met just after function name, it's considered that started by it __"inline"__ line contains
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
    - If __"("__ was met after separator (space) after function name, it's considered that started line for defining
        first function's argument (and "inline" line must contain expression (return something)).
        ```coffeescript
        function_name (4 + 8), arg_2, (3 + arg_3)
        ```
        - if empty inline-line was passed to function, it considers that it was launched without any argument:
            ```coffeescript
            function_name ()
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




# Decorators
- #### Syntax:
    - is just like in python:
        ```coffeescript
        @some_decorator
        a = def c, d -> return c + d

        @some_decorator; a = def c, d -> return c + d

        @some_decorator
        function calculate_difference var_1, var_2
            return var_2 - var_1
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

        try -> expression; expression_2 <- except Exception as inst -> expression <- finally -> expression
    ```




# Conditional expressions
- #### "if" conditional expression:
    Examples:
    - the most common:
        ```coffeescript
        if var_2 > 5
            function_name()
        ```
    - with inline line:
        ```coffeescript
        if (var_2 > 5)
            function_name()
        if(var_2 < 4)
            function_2_name()
        if(var_2 <
        4)
            function_3_name()
        ```
    - written in one line:
        ```coffeescript
        if var_1 > var_2 -> var_3 = var_2
        ```




# Inner implementation details:
- package consists from such main parts:
    - __tokens__ (list of all used in language tokens)
    - __scanner__ (scans souce code and creates list of found tokens (token stream))
    - __parser__ (scans list of found tokens (token stream), makes AST from it)
    - __modulule_creator__ (resulting AST packs into module, adds to sys.modules)
    - __package_finder__
        (finds .python files, packages (directories with `__init__.python`)
        from sys.path directories)
    - __organizer__
        (after calling "uses()" function launches all other components by order)
        there would be no difference for compiler: in which line of something is,
        the only matter for containing token's lines is for showing user as debug
        info
