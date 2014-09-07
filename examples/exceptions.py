
def exceptions_must_derive_from_exception():
    """
    As of Python 3.0 all exceptions must derive from BaseException.
    In practise you should make your exceptions a subclass of Exception.

    You can learn more about this in PEP 352.
    """
    class MyException(Exception):
        pass

    try:
        raise MyException
    except Exception:
        pass


def exceptions_have_different_scope():
    """
    As of Python 3.0 the caught exception is no longer accessible
    outside the except scope. You'll now also need to use the keyword
    'as' rather than a comma when catching an exception.

    You can learn more about this in PEP 3110.
    """
    try:
        raise ValueError('error')
    except Exception as exc:
        print(exc)

    try:
        exc
    except NameError:
        print("The variable 'exc' no longer exists here.")


def exceptions_have_traceback_attribute():
    """
    As of Python 3.0 each exception has a __traceback__ attribute that
    allows access to various relevant attributes regarding the exception
    and execution at the time of the exception.

    You can learn more about this in PEP 3134.
    """
    try:
        raise ValueError
    except Exception as exc:
        print("Exception occurred at line:", exc.__traceback__.tb_lineno)


def exceptions_can_be_implicitly_chained():
    """
    The following will print a traceback that includes both the
    original exception and the new exception that was raised while
    handling the original exception.
    """
    try:
        raise ValueError
    except Exception:
        raise Exception


def exceptions_can_be_explicitly_chained():
    """
    The following allows you to express that the new exception was
    directly caused by another exception.

    You can learn more about this in PEP 3134.
    """
    try:
        raise ValueError
    except Exception as exc:
        raise Exception from exc


def exceptions_can_be_suppressed():
    """
    As of Python 3.3 you can supress the original exception in a traceback.
    This is useful when you're catching an exception and you don't wish to
    expose that exception in the traceback. This can be used in a library
    that wishes to raise its own exception and hide the original exception
    that happened internally inside the library.

    You can learn more about this in PEP 409.
    """

    class CustomException(Exception):
        pass

    try:
        raise ValueError
    except Exception:
        raise CustomException from None
