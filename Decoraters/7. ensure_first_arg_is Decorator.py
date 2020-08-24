from functools import wraps


def first_age_dec(val):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"first value should be {val}"
            return func(*args, **kwargs)

        return wrapper

    return inner


@first_age_dec(10)
def sum_of_num(num1, num2):
    return num1 + num2


print(sum_of_num(10, 50))
print(sum_of_num(20, 40))  # first value should be 10
