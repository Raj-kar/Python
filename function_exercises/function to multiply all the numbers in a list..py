def multiply(list):
	m = 1
	for i in list:
		m *= i
	return m
 
print(multiply((8, 2, 3, -1, 7)))