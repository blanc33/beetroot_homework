from functools import wraps

class TypeDecorators:

    def to_int(self):
        @wraps(self)
        def wrapper(*args):
            try:
                return int(self(args)[0])
            except ValueError:
                return "Can't convert to int"
        return wrapper

    def to_str(self):
        @wraps(self)
        def wrapper(*args):
            try:
                return str(self(args)[0])
            except ValueError:
                return "Can't convert to str"
        return wrapper

    def to_bool(self):
        @wraps(self)
        def wrapper(*args):
            try:
                return bool(self(args)[0])
            except ValueError:
                return "Can't convert to bool"
        return wrapper

    def to_float(self):
        @wraps(self)
        def wrapper(*args):
            try:
                return float(self(args)[0])
            except ValueError:
                return "Can't convert to float"
        return wrapper

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True