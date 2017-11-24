Main details:



Main standards:
       Elegance:
               not overdosing with tokens, better using real words
       Similarity to Python, CoffeeScript code
       Usability:
               almost all may could be combined as user wishes
               all code could be written in one line, or could be written in
                       separate lines, depends on what developer think
                But often-used tasks may be written with more clear syntax than lesser-used ones.


Scopes and brackets:
        PythonScript uses line-based scoping.
            One expression must be on one line. But lines can be emulated by brackets "()" (all inside
            such brackets is considered as one line). Also line end can be emulated with ";", after it new
            line starts.
            WIth "->" we can emulate indent (EOL + indent, there is no separate token for indent
            because indent cannot be without new line), with "<-" - dedent (EOL + dedent).

       "{}" are ignored (you can place them where you want (except inside strings))
       "()" are used for grouping. All inside of them can be considered as one line or group.
       "[]" are using for taking arguments and slices


Collections types:
        Literals:
            Lists:
                list 1, 2, 3, def a, b -> return a + b <-, 4, 5, 6
                list 1, 2, 3, (def a, b -> return a + b), 4, 5, 6
                multiline list definition (will be readed until dedent):
                    list \
                        1, 2, 3, \
                        4, 5, 6
                using brackets:
                        (list 1, 2, 3
                    4, 5, 6)
                    # if line starts with "(", it will not be finished until ")"
                    # even dedent is ignored, not talking about "<-" or ";"
                    # also this line can be considered as "inline line", because
                    # "(" in the center of line will not be considered as end of current line
                    # and starting new one (what ";") does. In center of line it can have expression,
                    # that returns value, nothing other.
                    # And if "(" was on the start of real line (after indent if it was, of course),
                    # than it could have also statements and that line will not be finished until ")"
            Sets:
                set 1, 2, 10, 'a'
            Dicts:
                dict 1: 4, 5: b, 'new_value': 344
                dict  1: 4,  5: b,  8: c
                (dict  'a': 8,  22: 4,
                    23: 'ab')
        Running methods on collections literals:
            list 1, 2, 3, 4;  .reverse do  .some_method do

            set 1, 2, 3
            .union set_2

            (list 1, 2, 3, 4).reverse do
       Taking by index:
               Lists:
                    a = list 1, 2, 3, 4
                    a[1]  # will give 1
                    a [2]  # will give 2
                    a [-1]  # will give 4
                    a[-2]  # will give 3
               Tuples:
                       are taking analogically to Lists
               Sets, Dicts:
                       doesn't support

       Taking by key:
               Dicts:
                       a = d{}'a': 'b', 2: 3}
                       a['a']  # will give 'b'
                       a [2]  # will give 3
               Lists, Tuples, Sets:
                       doesn't support

       Taking slices:
               Lists:
                       a = l{1, 2, 3, 4, 'a'}
                       a[1..3]  # will give l[1, 2, 3]
                       a [2 .. -2]  # will give l[2, 3, 4]
                       a [1..-1 .. 2]  # will give l[1, 3, 'a']
               Tuples:
                       analogically to Lists.
               Sets, Dictionaries:
                       doesn't support


Generators:
       List generators:
               gen list x for x in somevariable}
               gen list x for x in l{1, 2, 3} if x != 2
               gen list i + 2 for i, v in (gen list i2 for i2 in range 4, 2)
       Tuple generators:
               same as list ones
       Dictionaries generators:
                gen dict k: v for k, v in zip var_1, var_2
                gen dict k: v for k, v in (zip var_1, var_2)
                gen dict   k: v   for k, v   in   zip var_1, var_2
                gen dict k: v for k, v in (zip var_1, var_2) if k > v
                gen dict   k: v   for k, v   in (zip var_1, var_2)   if k > v


Try/Except blocks:
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

        try -> expression; expression_2; except Exception as inst -> expression; finally -> expression


Functions:
        Definition:
                ```
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

                # if you want
                ```

        Wrong / correct definition:
                wrong:
                    ```
                    a = def (arg, args)    # because def waits for passing arguments, and here
                            expression     # data in brackets does not return anything
                    ```
                correct:
                    ```
                    a = def (arg), (arg + something)
                        expression
                    ```
        Running functions:
                ```
                a = def -> return 4
                a do    # will run function without arguments
                do a    # wrong syntax

                printer = def *args -> print args
                printer(arg_1, arg_2)
                printer arg_1, arg_2
                printer (arg_1, arg_2)    # wrong syntax. Expects argument, so "()" must return object or something
                ```
        Also they can be passed as arguments to other functions:
                ```
                l = def func, argument_2 -> func(); print argument_2
                l (def -> print "something"), 44
                l def -> print "something" <-, 'some word'
                (l def -> print "something" <-,    # grouping example
                    'some word')
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
