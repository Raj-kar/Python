def given_range(num):
	for i in range(3,9):   #exclude 9
		if(i == num):
			return f"{num} is in the list"
	return f"{num} is not in the list"

print(given_range(5))	 # 5 is in the list
print(given_range(9))    # 9 is not in the list