# sorted can use for sort list,tuple,dict .
# it's return a sorted copy of the input, not change the original list/tuple or dict !

# yoh ! let's see ~

nums = [55, 4, 1, 9, 65]  # list

print(sorted(nums))						# [1, 4, 9, 55, 65]
print(sorted(nums, reverse=True))		# [65, 55, 9, 4, 1]

# <----------------------------------------------------------> #

nums = (55, 4, 1, 9, 65)  # tuple

print(sorted(nums))		# [1, 4, 9, 55, 65]   # retuurn as a list
# also can reverse tuple


# <----------------------------------------------------------> #

user_list = [
    {"username": "Raj", "age": 19, "tweets": [
        'i love python', 'python is awesome'], "fav_colors":["blue", "red"]},
    {"username": "Raima", "age": 19, "tweets": []},
    {"username": "Monai", "age": 15, "tweets": [
        'i love to watch youtube', 'I love to Dance', 'I also loev to sing'], "fav_colors":["blue", "red"], "fav_no":1},
    {"username": "Babai", "age": 12, "tweets": []},
    {"username": "Rahul", "age": 17, "tweets": [
        'I\'m a pubg lover', 'I hate programming']},
]

# sorted using number of keys, probably we never use this :p
print(sorted(user_list, key=len))

print()

# sorted using name a-z, probably we use this :)
print(sorted(user_list, key=lambda user: user['username']))

print()

# sorted using number of tweets higher - lower, probably we use also this :)
print(sorted(user_list, key=lambda user: user['tweets'], reverse=True))


# <----------------------------------------------------------> #

song_list = [
    {"name": "play date", "duration": 5.23, "Playtime": 83},
    {"name": "Khulke jeena ka", "duration": 3.43, "Playtime": 93},
    {"name": "Hasi", "duration": 2.00, "Playtime": 73},
    {"name": "Dil Bechara", "duration": 3.03, "Playtime": 183},
    {"name": "ekta kotha bolbo", "duration": 4.10, "Playtime": 103},
]

print()

# sorted by song Duration, higher - lower, probably we use  this :)
print(sorted(song_list, key=lambda song: song['duration'], reverse=True))

print()

# sorted by number of song played, higher - lower, probably we use  this :)
print(sorted(song_list, key=lambda song: song['Playtime'], reverse=True))

by_play_time = sorted(
    song_list, key=lambda song: song['Playtime'], reverse=True)

print()

# print the song names and playtime from the sorted dict
for i in by_play_time:
    print(f"song {i['name']} played {i['Playtime']} times")

# output 
# song Dil Bechara date played 183 times
# song ekta kotha bolbo played 103 times
# song Khulke jeena ka played 93 times
# song play date played 83 times
# song Hasi played 73 times