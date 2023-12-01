import functools
from datetime import datetime


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        duration = (datetime.now() - start).total_seconds()
        print(f"Time: {duration}sec")

    return wrapper
