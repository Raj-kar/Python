value = int(input("Enter a number to check prime or not :: "))

count = 0

for i in range(1,value):
	if value % i == 0:
		count += 1

if count == 1:
	print(f"\n {value} is a prime number")
else:
	print(f"\n {value} is not a prime number")