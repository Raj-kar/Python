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

print(your_instructer)

# same thing using list comprehension 
print(["your instructer is " + name for name in names if len(name) < 5])

# <---------------------------------------------------->
