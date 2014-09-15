
x = 5

def new_nonlocal_keyword():
    """
    As of Python 3.0 you can use the 'nonlocal' keyword to refer
    to variables outside the current scope. This doesn't mean the
    global scope so the 'x = 5' above isn't relevant here.

    You can learn more about this in PEP 3104.
    """
    x = 4
    def f():
        nonlocal x
        x = 3
    f()
    print(x)  # This prints 3 instead of 4.


def print_is_no_longer_a_statement():
    """
    As of Python 3.0 the print statement has become a function. You
    can now call the print() function with various arguments to perform
    a print action.

    You can learn more about this in PEP 3105.
    """
    print("This is an example")

    print("These", "words", "are", "separated", "by", "plus", sep="+")

    print("This line ends with a bang: ", end="BANG\n")

    print("This prints to stderr instead of stdout", file=sys.stderr)

    # This prints abc
    print(*['a', 'b', 'c'], sep='')
