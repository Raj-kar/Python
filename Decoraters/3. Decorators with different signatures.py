def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"hey i am {name}"


@shout
def order(main, side):
    return f"Hey i need a {main} and also a {side}"


@shout
def say_hello(per1, per2, per3):
    return f"Hey {per1}, say hello to {per2} and {per3}"


@shout
def lol():
    return "lol"


print(greet("Raj"))
print(order(side="fries", main="chocolate"))
print(lol())
print(say_hello(per1="Raj", per3="Raima", per2="Monai"))





