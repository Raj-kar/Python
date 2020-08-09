e_list = []

def check_even(values):
	for i in values:
		if i % 2 == 0:
			e_list.append(i)
	return e_list


print(check_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))