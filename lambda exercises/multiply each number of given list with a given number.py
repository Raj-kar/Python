# Write a Python program that multiply each number of given list
# with a given number using lambda function. Print the result.

# i consider the number as 5
multiply_list = lambda *args: [arg*5 for arg in args]

nums = [1, 2, 3, 4, 5]

print(multiply_list(*nums))
