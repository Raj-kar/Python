def factorial(num):
	fact = 1
	for i in range(1,num+1):
		fact *= i
	return fact

print(factorial(5))  #120
print(factorial(0))  #1