"""Code tries to be valid, but some definitions will be omitted.
"""


function some_extra_test
    result = func_2 arg_1 arg_2 (func_3 arg_3)
    # here we launched 'func_2' with args:
    #       'arg_1', 'arg_2', result of calling 'func_3' with 'arg_3'
    return result


function test_2
    ###Shows examples of Array definitions, working with them.
    ###

    list_1 = list 1, arg_3, (func_3 33.8), 4, 2
    # we just defined list

    instance_1 = ClassName1 arg_1, (list 1, 2, 3), arg_2

    instance_2 = ClassName1 arg_1, list ->
        1, 2, 3, 4, (func_3 284.5), 8,
        7, arg_2, 22.4
    # here '->' means that list will be defined as block, so we must make
    # end of line and indent. Block of list arguments will be finished
    # when dedent will be met

    instance_3 = ClassName1 arg_1 arg_2 arg_3 list ->
        1 2 3 4 (func_3 284.5) 8 22 11
    # commas in list definition are not required,

    instance_4 = ClassName1 arg_1, arg_2, arg_3, list ->
        1 2 3 4 (func_3 284.5) 8 22 11
        8 22 11 16 4 <-
