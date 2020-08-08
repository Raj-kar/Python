value = input("Enter interger/string to check panildrome or not :: ")

if(value == value[::-1]):
	print(f"{value} is panildrome")
else:
	print(f"{value} is not panildrome")