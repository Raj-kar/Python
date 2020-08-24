from functools import wraps


def ensure_ice_creme(val):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] != val:
                return "First argument must be ice creme !"
            return func(*args, **kwargs)

        return wrapper

    return inner


@ensure_ice_creme("ice creme")
def order(food1, food2):
    return f"you {food1} and {food2} are ready sir !!"


print(order("ice creme", "pizza"))  # you ice creme and pizza are ready sir !!
print(order("rice", "burger"))  # First argument must be ice creme !
