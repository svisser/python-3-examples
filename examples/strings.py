import collections
import collections.abc


def strings_have_format_map_method():
    """
    As of Python 3.2 you can use the .format_map() method on a string object
    to use mapping objects (not just builtin dictionaries) when formatting
    a string.
    """

    class Default(dict):

        def __missing__(self, key):
            return key

    print("This prints the keys: {a} {key2}".format_map(Default(a="key1")))

    mapping = collections.defaultdict(int, a=2)
    print("This prints the value 2000: {a}{b}{c}{d}".format_map(mapping))

    class MyMapping(collections.abc.Mapping):

        def __init__(self):
            self._data = {'a': 'A', 'b': 'B', 'c': 'C'}

        def __getitem__(self, key):
            return self._data[key]

        def __len__(self):
            return len(self._data)

        def __iter__(self):
            for item in self._data:
                yield item

    mapping = MyMapping()
    print("This prints ABC: {a}{b}{c}".format_map(mapping))
