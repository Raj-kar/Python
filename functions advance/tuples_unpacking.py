# normal way

def sum_of_nums(*args):
	total = 0
	for i in args:
		for j in i:
			total += j
	print(total)

num = [1,2,3]
sum_of_nums(num)

# advance unpacking way

def sum_of_nums(*args):
	total = 0
	for i in args:
		total += i
	print(total)

num = [1,2,3]
sum_of_nums(*num) # pass with *