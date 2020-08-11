names = ["Raj", "Raima", "Rahul", "Monai", "Babai"]

start_with_R = list(filter(lambda name: name[0] == "R", names))

print(start_with_R)  # ['Raj', 'Raima', 'Rahul']

# <---------------------------------------------------->

nums = range(11)		# we get 0 to 10 for range .

isEven = list(filter(lambda x: x % 2 == 0, nums))

print(isEven)			# [0, 2, 4, 6, 8, 10]

# <---------------------------------------------------->

names = ["Raj", "Raima", "Rahul", "Monai", "Babai", "Joy", "Aman"]

your_instructer = list(map(lambda name: "your instructer is " +
                           name, filter(lambda name: len(name) < 5, names))) 
									# ['your instructer is Raj', 'your instructer is Joy', 'your instructer is Aman']

print(your_instructer)

# same thing using list comprehension
print(["your instructer is " + name for name in names if len(name) < 5])	
									#['your instructer is Raj', 'your instructer is Joy', 'your instructer is Aman']

# <---------------------------------------------------->

user_list = [
    {"username": "Raj", "age": 19, "tweets": [
        'i love python', 'python is awesome']},
    {"username": "Raima", "age": 19, "tweets": []},
    {"username": "Monai", "age": 15, "tweets": [
        'i love to watch youtube', 'I love to Dance']},
    {"username": "Babai", "age": 12, "tweets": []},
    {"username": "Rahul", "age": 17, "tweets": [
        'I\'m a pubg lover', 'I hate programming']},
]


no_tweets = list(map(lambda user: user['username'] + " has zero tweet",
                     filter(lambda user: not user['tweets'], user_list)))

print(no_tweets)		# ['Raima has zero tweet', 'Babai has zero tweet']

# same thing using list comprehension

print([user['username'] + " has zero tweet" for user in user_list if not user['tweets']])