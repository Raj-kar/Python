def palindrome(val):
	val = str(val)
	if val == val[::-1]:  #use slice technique reverse the given value
		prime(int(val))
	else:
		print(f"{val} is not a palindrome number")

def prime(limit):
	count = 0
	for i in range(2,limit//2):
		if limit % i == 0:
			count += 1
	if count == 0:
		print(f"{limit} is a PalPrime number ")
	else:
		print(f"{limit} is not a PalPrime number ")

palindrome(353)
palindrome(121)