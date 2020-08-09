# Create an outer function that will accept two parameters a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


def outer(a, b):
    def inner():
        return a+b
    return inner()+5


print(outer(5, 10))
