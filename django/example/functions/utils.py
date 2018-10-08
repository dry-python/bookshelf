from functools import wraps


def apply(f):

    def decorator(g):

        @wraps(g)
        def wrapper(*args, **kwargs):
            return f(g(*args, **kwargs))

        return wrapper

    return decorator
