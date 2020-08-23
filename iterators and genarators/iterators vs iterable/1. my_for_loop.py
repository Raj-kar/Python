def my_for(iterable, func=print):
    iterator = iter(iterable)
    while True:
        try:
            res = next(iterator)
        except StopIteration:
            break
        else:
            if func == print:
                print(res, end=" ")
            else:
                func(res)

    print()


def square(val):
    print(val * 2, end=" ")


def qube(val):
    print(val ** 3, end=" ")


my_for("Python")
my_for([1, 2, 3, 4, 5], square)
my_for([1, 2, 3, 4, 5], qube)
