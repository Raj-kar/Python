def hypen_sorted(str_list):
	str_list = str_list.split('-')
	str_list.sort()

	return '-'.join(str_list)

print(hypen_sorted("green-red-black-white"))