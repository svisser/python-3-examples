
def get_uppercase():
    for c in range(26):
        yield chr(65 + c)


def get_lowercase():
    for c in range(26):
        yield chr(97 + c)


def get_uppercase_and_lowercase():
    """
    As of Python 3.3 you can use 'yield from' to yield values from
    other generators. You can use the following to print the uppercase
    and lowercase characters in the English alphabet:

    for c in get_uppercase_and_lowercase():
        print(c)
    """
    yield from get_uppercase()
    yield from get_lowercase()
