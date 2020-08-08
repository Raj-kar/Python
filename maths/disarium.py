value = input("Enter a vlaue to check Disarium number or not :: ")

count = 1
s = 0

if value:
	for i in value:
		s += int(i)**count
		count += 1	

	if s == int(value):
		print(f"{value} is a Disarium number ..!")
	else:
		print(f"{value} is not a Disarium number ..!")
else:
	print("Enter a proper value ..!")

# 175,135,89 etc ..! [sum of cubes are same]