def add(num1 = 1 ,num2 = 1):
	return num1 + num2

def subtract(num1 = 1 ,num2 = 1):
	return num1 - num2

def multiplication(num1 = 1 ,num2 = 1):
	return num1 * num2

def division(num1 = 1 ,num2 = 1):
	return num1 / num2

def math(num1 , num2 , fun = add):
	return fun(num1,num2)

print(math(10,40))   #default perfrom add operation !
print(math(10,20,subtract))
print(math(10,20,multiplication))