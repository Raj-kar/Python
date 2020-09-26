# pattern --> 1

for i in range(1,10,2):
	for j in range(i,10,2):
		print(j,end=" ")
	for k in range(1,i,2):
		print(k,end=" ")
	print()

# output -->
# 1 3 5 7 9 
# 3 5 7 9 1 
# 5 7 9 1 3 
# 7 9 1 3 5 
# 9 1 3 5 7 

# pattern --> 2

for i in range(5,0,-2):
	for j in range(i,0,-1):
		print(i,end=" ")
	print()

# output -->
# 5 5 5 5 5 
# 3 3 3 
# 1 

# pattern --> 3

for i in range(1,10,2):
	for j in range(i,0,-2):
		print(i,end=" ")
	print()

# output -->
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9 

# pattern --> 4

k = 15
for i in range(5,0,-1):
	for j in range(1,i+1):
		print(k,end=" ")
		k -= 1;
	print()

# output -->
# 15 14 13 12 11 
# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1
