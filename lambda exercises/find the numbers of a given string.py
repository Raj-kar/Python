# Write a Python program to find the numbers of a given string and store them in a list,
# display the numbers which are bigger than the length of the list in sorted form.
# Use lambda function to solve the problem.

find_number = lambda *args: sorted(
    [arg for arg in args if arg != str(arg)])

nums = [15, 21, 3, "Css", 54, "Java", 13, "Python"]

print(find_number(*nums))
