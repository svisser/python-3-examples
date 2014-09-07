import inspect


def functions_can_have_annotations(a: int, b: int) -> int:
    """
    As of Python 3.0 you can annotate parameters and return
    values of functions with expressions. These are optional and
    they don't influence the execution of the Python code.

    You can learn more about these in PEP 3107.
    """
    return a + b


def function_annotations_can_be_accessed():
    """
    You can use the '__annotations__' attribute to obtain
    the annotations. The return value's annotation can be
    accessed using the 'return' key.

    As of Python 3.3 you can also use inspect.signature to
    obtain the annotations.
    """
    print(functions_can_have_annotations.__annotations__)
    # Prints: {'a': <class 'int'>, 'return': <class 'int'>, 'b': <class 'int'>}

    sig = inspect.signature(functions_can_have_annotations)
    print(sig)
    # Prints: (a:int, b:int) -> int

    print(sig.return_annotation)
    # Prints: <class 'int'>

    for name, parameter_object in sig.parameters.items():
        print(name, parameter_object.annotation)
    # Prints:
    # a <class 'int'>
    # b <class 'int'>
