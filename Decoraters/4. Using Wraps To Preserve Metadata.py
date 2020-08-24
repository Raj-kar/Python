# def log_function_data(func):
#     def wrapper(*args, **kwargs):
#         """ A wrapper of add function"""
#         print(f"you are using here {func.__name__}")
#         print(f"the doc of {func.__name__} is {func.__doc__}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log_function_data
# def add(num1, num2):
#     """ Sum two numbers """
#     return num1 + num2
#
#
# print(add(10, 20))

# without using wraps function we loss the add name and doc
# print(add.__name__)     # wrapper
# print(add.__doc__)      # A wrapper of add function


# using WRAPS so, we don't loss any data
from functools import wraps


def log_function_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ A wrapper of add function"""
        print(f"you are using here {func.__name__}")
        print(f"the doc of {func.__name__} is {func.__doc__}")
        return func(*args, **kwargs)

    return wrapper


@log_function_data
def add(num1, num2):
    """ Sum two numbers """
    return num1 + num2


print(add(10, 20))
print(add.__name__)  # add
print(add.__doc__)  # Sum  two numbers
