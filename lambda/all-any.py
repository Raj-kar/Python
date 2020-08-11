nums = [0, 1, 2, 3]

# False because 0 is Falsy ! If all values are truty, it returns truthy !
print(all(nums))
print(any(nums))  # True because if any one is ture, it's return true.

nums = [1, 2, 3]

print(all(nums))  # True
print(any(nums))  # True

nums = []

print(all(nums))  # Return True, if empty
print(any(nums))  # Return False, if empty

nums = [2, 4, 6, 8, 10]
# all num can divisible by 2, so True
print(all([num % 2 == 0 for num in nums]))

nums = [2, 4, 6, 7, 10]
# all num can't divisible by 2, so False
print(all([num % 2 == 0 for num in nums]))
# any of the num can divisible by 2, so true
print(any([num % 2 == 0 for num in nums]))

names = ["Raj", "Raima", "Rahul", "Rohit", "Ricky", "Ramesh"]

# True because all names start with "R"
print(all(name[0] == "R" for name in names))

names = ["Raj", "Raima", "Rahul", "Babai", "Ricky", "Monai"]

# False because all names not start with "R"
print(all(name[0] == "R" for name in names))

# True because any one the name not start with "R"
print(any(name[0] == "R" for name in names))
