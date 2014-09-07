from functools import singledispatch


@singledispatch
def function(arg):
    return "Type of argument: {}".format(type(arg))


@function.register(list)
def function_list(arg):
    return "Size of list: {}".format(len(arg))


@function.register(int)
def function_int(arg):
    return "Value of int: {}".format(arg)


@function.register(set)
def function_set(arg):
    return "Size of set: {}".format(len(arg))


def example_with_singledispatch():
    """
    As of Python 3.4 you can use functools.singledispatch to
    call an appropriate function depending on the type of the argument.

    You can learn more about this in PEP 443.
    """
    print(function(3))
    print(function([1, 2, 3]))
    print(function(set([1, 2, 3])))
    print(function(object()))
