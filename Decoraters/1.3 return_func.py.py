# We can return funcs from other funcs

from random import choice


def make_laugh():
    def laugh():
        return choice(("HAHAHAHA", "hehehehe", "Lol"))

    return laugh


sound_laugh = make_laugh()
print(sound_laugh())

# also can use
print(make_laugh()())
