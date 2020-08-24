# # We can nest functions inside one another


from random import choice


def greet_msg(name):
    def greet():
        return choice(("Hi ", "Bye ", "Go away "))

    return greet() + name


print(greet_msg("Raj"))
