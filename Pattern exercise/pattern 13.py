# Write a Python program to construct the following pattern, using a nested loop number.

# Expected Output:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

row = int(input("Enter a range: "))

for i in range(1,row+1):
	print(f"{i}"*i)