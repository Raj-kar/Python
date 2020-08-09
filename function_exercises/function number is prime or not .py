def prime(num):
	count = 0
	for i in range(2,num):
		if num % i == 0:
			count += 1
	if count == 0:
		return True
	else:
		return False

print(prime(7))
print(prime(10))