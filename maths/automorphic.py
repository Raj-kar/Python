value = input("Enter a number to check automorphic or not :: ")

automorphic = int(value)**2

if (str(automorphic)[-(len(value)):]) == value:
	print(f"{value} is automorphic number")
else:
	print(f"{value} is not automorphic number")


# In mathematics an automorphic number (sometimes referred to as a circular number)
# is a number whose square "ends" in the same digits as the number itself.
# For example, 5^2 = 25 , 6^2 = 36 , 76^2 = 5776 , 376^2 = 141276