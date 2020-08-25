class Robot(object):
    """Robot can do your different types of works"""

    def __init__(self, name, battery=100, skills=[]):
        self.name = name
        if battery > 100:
            raise ValueError("Maximum charge should be 100 !")
        self.battery = battery
        self.skills = skills

    def charge(self, percentage=100):
        if percentage > 100:
            raise ValueError("Maximum charge should be 100 !")
        self.battery = percentage
        return "battery charged !"

    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"BIP BIP BIP ! MY name is {self.name}"
        return "Oh noo! charge me !"

    def learn_skill(self, new_skill, cost_to_learn):
        if self.battery >= cost_to_learn:
            self.battery -= cost_to_learn
            self.skills.append(new_skill)
            return f"BIP BIP BIP !!.. Now I know how to {new_skill}"
        return f"Oh noo! charge me for learn {new_skill}"


# self Test !

# rob1 = Robot("Raj", battery=90)
# print(rob1.name)
# rob1.charge()
# print(rob1.battery)
# print(rob1.skills)
# print(rob1.say_name())
# print(rob1.learn_skill("dance", 49))
# print(rob1.say_name())
# print(rob1.charge())
# print(rob1.learn_skill("sing", 89))
# print(rob1.skills)
