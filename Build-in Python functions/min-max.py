# max use for search the maximum value in list,tuple,str,dict and min for minimum value

print(max(1, 2, 3))		# 3

print(min(1, 2, 3))		# 1

nums = [1, 3, 41, 4, 83]

print(max(nums))		# 83

print(min(nums))		# 1

# also we can pass tuple

names = ["Raj", "Rahul", "Raimaa", "Chandrashree"]

print(max(names, key=lambda n: len(n)))		# Chandrashree

print(min(names, key=lambda n: len(n)))		# Raj

# max-min dict
song_list = [
    {"name": "play date", "duration": 5.23, "Playtime": 83},
    {"name": "Khulke jeena ka", "duration": 3.43, "Playtime": 93},
    {"name": "Hasi", "duration": 2.00, "Playtime": 73},
    {"name": "Dil Bechara", "duration": 3.03, "Playtime": 183},
    {"name": "ekta kotha bolbo", "duration": 4.10, "Playtime": 103},
]

# most played song {'name': 'Dil Bechara date', 'duration': 3.03, 'Playtime': 183}
print(max(song_list, key=lambda s: s['Playtime']))

# less played song {'name': 'Hasi', 'duration': 2.0, 'Playtime': 73}
print(min(song_list, key=lambda s: s['Playtime']))

# for print only most or less played song name
print(min(song_list, key=lambda s: s['Playtime'])['name'])  # Hasi
print(max(song_list, key=lambda s: s['Playtime'])['name'])  # Dil Bechara date
