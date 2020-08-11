
def add(*args):
	total_sum = 0
	for num in args:
		total_sum += num
	return total_sum

print(add(10,20))
print(add(10,20,30,40,50))
