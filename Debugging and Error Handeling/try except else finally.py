
def division(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("Can't Divisible a number by zero")
    except TypeError:
        print("num1 and num2 must be a string")
    else:						# if except not execute, then else execute
        print(f"{num1} divide by {num2} = {result}")
    finally:
        print("Bye ..!")


division(10, 2)				# 10 divide by 2 = 5.0
print()						# Bye ..!

division(10, 0)				# Can't Divisible a number by zero
print()						# Bye ..!

division(10, 'a')			# num1 and num2 must be a string
print()						# Bye ..!

division('a', 'a')			# num1 and num2 must be a string
print()						# Bye ..!
