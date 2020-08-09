def count_upper_lower(str):
	# str = str.replace(" ","")
	upper = 0
	lower = 0
	for i in str:
		if i.isupper():
			upper += 1
		elif i.islower():
			lower += 1
		else:
			pass

	print(f"No. of Upper case characters : {upper}")
	print(f"No. of Lower case characters : {lower}")


count_upper_lower("The quick Brow Fox")
