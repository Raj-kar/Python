# Write a Python program to square and cube every number in a given list of integers using Lambda.

nums = [1, 2, 3, 6]

square_cube = lambda *args: print(
    list(zip([arg*arg for arg in args], [arg**3 for arg in args])))

square_cube(*nums)	# [(1, 1), (4, 8), (9, 27), (36, 216)]

# we can also use map for this

cube = list(map(lambda x: x ** 3, nums))  # for cube
square = list(map(lambda x: x ** 2, nums))  # for square

print(square, cube)  # [1, 4, 9, 36] [1, 8, 27, 216]
