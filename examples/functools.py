from functools import singledispatch, total_ordering


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


def example_with_total_ordering():
    """
    As of Python 3.2 you can use functools.total_ordering to
    compare instances of any class as long as you've implemented
    the __eq__() method and one of __lt__(), __le__(), __gt__(),
    or __ge__().
    """
    @total_ordering
    class Person:

        def __init__(self, age):
            self.age = age

        def __eq__(self, other):
            return self.age == other.age

        def __lt__(self, other):
            return self.age < other.age

        def __repr__(self):
            return "Person (age: {})".format(self.age)

    print(Person(age=20) < Person(age=30))
    print(Person(age=20) > Person(age=30))
    print(Person(age=20) <= Person(age=30))
    print(Person(age=20) >= Person(age=30))
    print(Person(age=20) == Person(age=30))
