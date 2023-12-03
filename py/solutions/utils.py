import functools
from datetime import datetime


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        duration = (datetime.now() - start).total_seconds()
        print(f"`{func.__name__}` time: {duration}sec")
        return result

    return wrapper
