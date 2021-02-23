import inspect
import re

__functions = []

def apply_on(pyfile):
    pattern = re.compile("def (.*)\(")
    for i, line in enumerate(open(pyfile)):
        for match in re.finditer(pattern, line):
            __functions.append(match.groups()[0])


def private(fn):
    global __functions

    def _restrict(*args, **kwargs):
        caller = inspect.stack()[1].function
        if caller not in __functions:
            raise NameError("Private function called")
        else:
            return fn(*args, **kwargs)
    return _restrict

