from functools import wraps


def no_more_than_three(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 3:
            # raise ValueError("Not more than three values accepted")
            return "Not more than three values accepted"  # also can use raise error
        return func(*args, **kwargs)

    return wrapper


@no_more_than_three
def sum_of_three_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total


print(sum_of_three_numbers(10, 20, 30, 90))  # Not more than three values accepted
print(sum_of_three_numbers(10, 20, 30))  # 60
