def palindrome(val):
	val = str(val)
	if val == val[::-1]:
		prime(int(val))

def prime(limit):
	count = 0
	for i in range(2,limit//2):
		if limit % i == 0:
			count += 1
	if count == 0:
		print(limit,end=" ")

for i in range(1,1000):
	palindrome(i)
