# Write a Python program to sort a list of tuples using Lambda


sort_tuple = lambda t: print(tuple(sorted(t)))

t = (3, 5, 4, 1)

sort_tuple(t)  # (1, 3, 4, 5)

sort_tuple((3, 65, 2, 11, -3, 6))  # (-3, 2, 3, 6, 11, 65)
