# We can also pass arguments and return funcs from other funcs

from random import choice


def make_laugh(name):
    def laugh():
        return choice(("HAHAHAHA ", "hehehehe ", "Lol ")) + name  # we can access parent class variable like name,
        # also known ass closures

    return laugh


sound_laugh = make_laugh("Raj")
print(sound_laugh())

# also can use
print(make_laugh("Raima")())
