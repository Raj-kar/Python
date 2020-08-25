# Different ways for import modules

import random
print(random.choice(["Python","Java","C","Css","JavaScript","Html5"]))

x = ["Python","Java","C","Css","JavaScript","Html5"]
print(random.sample(x, len(x)))

print(random.uniform(20, 60))			# 27.46206324887144	[changes everytime, return a value between 20 59]

print()


from random import choice,sample
print(choice(["Python","Java","C","Css","JavaScript","Html5"]))
print(sample(x, len(x)))

print()


import random as rand
print(rand.choice(["Python","Java","C","Css","JavaScript","Html5"]))
print(rand.sample(x, len(x)))

print()


from random import choice as lang_ch, sample as shuffle
print(lang_ch(["Python","Java","C","Css","JavaScript","Html5"]))
print(shuffle(x, len(x)))



# every time value changes

# Html5
# ['JavaScript', 'Java', 'C', 'Html5', 'Python', 'Css']

# Python
# ['C', 'Java', 'Css', 'Python', 'Html5', 'JavaScript']

# C
# ['JavaScript', 'C', 'Css', 'Java', 'Html5', 'Python']

# JavaScript
# ['Java', 'C', 'Css', 'Html5', 'Python', 'JavaScript']