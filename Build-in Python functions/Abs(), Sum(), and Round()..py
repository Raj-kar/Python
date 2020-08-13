# abs() in Python

# The abs() function is used to return the absolute value of a number.
# The argument can be an integer, a floating point number or a complex number.
# If the argument is an integer or floating point number, abs() returns the
# absolute value in integer or float.

print(abs(-23))			# 23
print(abs(23))			# 23
print(float(abs(93)))	# 93.0

# fabs() in Python

# The Python fabs function is one of the Python Math function, which returns the
# absolute value ((Positive value) of the specified expression or a specific number.
# Here, f refers to float.

import math

print(math.fabs(-13))	# 13.0
print(math.fabs(13))	# 13.0

# sum() in python
# the sum() function returns a number, the sum of all items in an iterable.

# print(sum([1,2,4,5]))		# error because it's not ittarable.
print(sum([1,2,4,5]))		# 12
print(sum([1,2,3],10))		# 16,because here,sum of 1+2+3 is added with 10 !

# round() in python

# Round() Round() is a built-in function available with python. It will return you
# a float number that will be rounded to the decimal places which are given as input.
# If the decimal places to be rounded are not specified, it is considered as 0, and it
# will round to the nearest integer.

print(round(1.13971271))		# 1
print(round(1.13971271,2))		# 1.4
print(round(1.627497272))		# 2
print(round(1.427497272,3))		# 1.427
print(round(9.9999999999999999999999999999999999999999999999999999999999,15))	#10.0  [need super comp :p]

