import inspect
import re

__functions = []

def apply_on(pyfile):
    '''
    Call it at the start of your module. The arg should be __file__.
    Usage:
    apply_on(__file__)
    '''
    pattern = re.compile("def (.*)\(")
    for i, line in enumerate(open(pyfile)):
        for match in re.finditer(pattern, line):
            __functions.append(match.groups()[0])


def private(fn):
    '''
    You need to add @private decorator to whichever function or class method
    that you want to make private.
    '''
    global __functions

    def _restrict(*args, **kwargs):
        caller = inspect.stack()[1].function
        if caller not in __functions:
            raise NameError("Private function called")
        else:
            return fn(*args, **kwargs)
    return _restrict

