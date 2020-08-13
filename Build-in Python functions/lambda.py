# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable
square2 = lambda num: num * num

# Another lambda
add = lambda a,b: a + b

# Executing the lambdas
print(square2(7))
print(add(3,10))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)