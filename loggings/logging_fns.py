from functools import wraps
import inspect


def log(func):
    @wraps(func)
    def logging(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e
    return logging