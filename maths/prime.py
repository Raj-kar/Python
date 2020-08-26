value = int(input("Enter a number to check prime or not :: "))

count = 0

for i in range(2,(value//2)+1):
	if value % i == 0:
		count += 1

if count == 0:
	print(f"\n {value} is a prime number")
else:
	print(f"\n {value} is not a prime number")