
def iterable_unpacking():
    """
    As of Python 3.0 you can use an iterable to unpack a sequence of
    elements. In Python 2.x you could already write:

        a, b = (1, 2)

    to obtain a = 1 and b = 2 but you can now also use iterables.

    You can learn more about this in PEP 3132.
    """
    a, *b, c = [1, 2, 3, 4, 5]
    # a = 1
    # b = [2, 3, 4]
    # c = 5

    x, *xs = range(10)
    # x = 0
    # xs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    x, y, z, *xs, k = range(10)
    # x = 0
    # y = 1
    # z = 2
    # xs = [3, 4, 5, 6, 7, 8]
    # k = 9

    *a, = range(10)
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for a, b, c, *n in [range(10)]:
        print(a, b, c)  # prints 0 1 2
