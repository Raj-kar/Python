from functools import wraps


def only_int(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not all(True if type(num) != str else False for num in args):
            return "only integer values supported !"
            # return ValueError("Only integer values supported")
        return func(*args, **kwargs)

    return wrapper


@only_int
def add_int(*args):
    total = 0
    for i in args:
        total += i
    return total


print(add_int(10, 20, 'a'))  # only integer values supported !
print(add_int(10, 20, 40, 1))  # 71
print(add_int('a', '1', '2'))  # only integer values supported !
