from functools import wraps
from time import time


def speed_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        stop_time = time()
        print(f"execution of {func.__name__} takes {stop_time - start_time} sec")
        return result

    return wrapper


@speed_test
def sum_of_nums():
    return sum(x for x in range(99))


@speed_test
def sum_of_nums_2():
    return sum([x for x in range(99)])


@speed_test
def sum_of(num1, num2):
    return num1 + num2


print(sum_of_nums())
print(sum_of_nums_2())
print(sum_of(10, 12))
