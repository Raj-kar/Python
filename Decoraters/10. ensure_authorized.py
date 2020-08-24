from functools import wraps


def ensure_auth(func):
    @wraps(func)
    def wrapper(*args):
        if "Raj" not in args:
            return f"Hey, you is not authorized"
        return func(*args)

    return wrapper


@ensure_auth
def welcome(name):
    return f"Welcome sir, {name}"


print(welcome("Rahul"))  # Hey, Rahul is not authorized
print(welcome("Raj"))  # Welcome sir, Raj
