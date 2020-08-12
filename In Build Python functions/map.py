names = ["Raj", "Raima", "Rahul", "Monai", "Babai"]

upper_case = list(map(lambda name: name.upper(), names))

print(upper_case)	#['RAJ', 'RAIMA', 'RAHUL', 'MONAI', 'BABAI']

# <---------------------------------------------------->

nums = [1, 2, 3, 4, 5]

nums_square = list(map(lambda x: x*x, nums))

print(nums_square)		#[1, 4, 9, 16, 25]

# <---------------------------------------------------->

names = ["Raj", "Raima", "Rahul", "Monai", "Babai"]

start_with_R = list(map(lambda name: name[0] == "R",names))

print(start_with_R)		#[True, True, True, False, False]

		# if we want the name, insted of True, False - We can use Filter ! {check filter.py for more ! }