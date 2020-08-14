# Write a Python program to find numbers divisible by nineteen,
# or thirteen from a list of numbers using Lambda.

divisible = lambda *args: [num for num in args if num %
                           19 == 0 or num % 13 == 0]

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(divisible(*nums))
