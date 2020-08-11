# reversed reverse list,tuple,str,range etc

for i in range(10):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9

print()

for i in reversed(range(10)):
    print(i, end=" ")  # 9 8 7 6 5 4 3 2 1 0

print()

# < --------------------------------------------------------------- > #

# return list_reverseiterator object, so convert to list !
print(list(reversed([1, 2, 3, 5, 6])))

# ['n', 'o', 'h', 't', 'y', 'P', ' ', 'o', 'l', 'l', 'e', 'H']
print(list(reversed("Hello Python")))

for i in reversed("Hello Python"):
    print(i, end="")		# nohtyP olleH

print()

# < --------------------------------------------------------------- > #

# use can also reversed a list , probably not such a usefull ! But you can :p
song_list = [
    {"name": "play date", "duration": 5.23, "Playtime": 83},
    {"name": "Khulke jeena ka", "duration": 3.43, "Playtime": 93},
    {"name": "Hasi", "duration": 2.00, "Playtime": 73},
    {"name": "Dil Bechara", "duration": 3.03, "Playtime": 183},
    {"name": "ekta kotha bolbo", "duration": 4.10, "Playtime": 103},
]

print(list(reversed(song_list)))

# [{'name': 'ekta kotha bolbo', 'duration': 4.1, 'Playtime': 103}, {'name': 'Dil Bechara',
# 'duration': 3.03, 'Playtime': 183}, {'name': 'Hasi', 'duration': 2.0, 'Playtime': 73},
# {'name': 'Khulke jeena ka', 'duration': 3.43, 'Playtime': 93}, {'name': 'play date', 'duration': 5.23,
#  'Playtime': 83}]
