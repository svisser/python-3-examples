
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
