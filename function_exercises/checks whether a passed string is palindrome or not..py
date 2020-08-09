def palindrome(val):
	val = str(val)
	if val == val[::-1]:  #use slice technique reverse the given value
		return True
	else:
		return False

print(palindrome(121))
print(palindrome("madam"))
print(palindrome("wow"))
