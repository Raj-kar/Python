# . Write a Python program which takes two digits m (row) and n (column) as input
# and generates a two-dimensional array. The element value in the i-th row and j-th
# column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

array = [[col for col in range(4)] for row in range(3)]		  # list comprehension !

for i in range(3):
	for j in range(4):
		array[i][j] = i*j


print(array)

# you can take any input ...!