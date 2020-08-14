# Write a Python program that removes the positive numbers from a given list of numbers.
# Sum the negative numbers and print the absolute value using lambda function. Print the result.

remove_positive = lambda *args : abs(sum([arg for arg in args if arg < 0]))

print(remove_positive(*[1,2,3,-1,-4,-6]))		# 11


nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]		# 32

print(remove_positive(*nums))