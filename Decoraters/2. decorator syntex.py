# def be_politer(func):
#     def wrapper():
#         print("Hey nice to meet you !")
#         func()
#         print("Have a Good day")
#
#     return wrapper
#
#
# def greet():
#     print("Hey My name is Raj !")
#
#
# def rage():
#     print("I hate you !")
#
#
# # without decorators
# wrapper_greet = be_politer(greet)
# wrapper_greet()


# Using Decorators


def with_polite(func):
    def wrapper():
        print("nice to see you")
        print("what about you !")
        func()

    return wrapper


@with_polite  # decorator - its mean [ hello = with_polite(hello) ]
def hello():
    print("let's go somewhere and talk")


@with_polite  # decorator - its mean [ bye = with_polite(bye) ]
def bye():
    print("I am busy, call you later")

# so we can now directly call hello and bye. python done all the heavy lifting at the backend.


hello()
bye()
