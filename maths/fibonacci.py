value = input("Enter range for Fibonacci series :: ")

a = 0
b = 1

print(" 0 1 ",end="")
for i in range(int(value)-2):
	c = a + b
	a,b = b,c
	
	print(c,end=" ")

