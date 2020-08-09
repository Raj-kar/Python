def calculate_sum(num):
	if num:
		return num + calculate_sum(num-1)
	else:
		return 0


res = calculate_sum(10)
print(res)
