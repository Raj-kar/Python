from functools import wraps


def ensure_no_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("now kwargs accepted !")
        return func(*args)

    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"Say hello to {name}")


greet("Raj")  # Say hello to Raj
greet(name="Raj")  # ValueError: now kwargs accepted !
