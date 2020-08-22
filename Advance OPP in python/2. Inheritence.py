class User:
    _active_user = 0

    def __init__(self, first, last, age):
        User._active_user += 1
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"

    def short_name(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, item):
        return f"{self.full_name()} likes {item}."

    def is_young(self):
        return self.age < 20

    def logout(self):
        User.active_user -= 1
        return f"{self.first} logged out !"

    def happy_birthday(self):
        self.age += 1
        return f"Hey {self.first}! Happy Birthday :)"

    @classmethod
    def active_user(cls):
        return f"No of active user {cls._active_user}"


class Moderator(User):
    _active_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator._active_mods += 1

    @classmethod
    def active_mods(cls):
        return f"No of active mods {cls._active_mods}"


print(User.active_user())  # No of active user 0

p1 = User("Raj", "Kar", 25)
p2 = User("Monai", "Roy", 16)

print(User.active_user())  # No of active user 2

m1 = Moderator("Raima", "Karmakar", 19, "philosophy")

print(User.active_user())  # No of active user 3

print(Moderator.active_mods())  # No of active mods 1

m2 = Moderator("Rahul", "Roy", 49, "code")

print(Moderator.active_mods())  # # No of active mods 2
