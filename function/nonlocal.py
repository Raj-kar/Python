def outer():
	count = 0 
	def inner():
		nonlocal count   # for acess non-global variables !
		count += 1
		return count
	return inner()

print(outer())