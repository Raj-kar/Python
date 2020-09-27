# # pattern --> 1

for i in range(1,10,2):
	for j in range(i,10,2):
		print(j,end=" ")
	for k in range(1,i,2):
		print(k,end=" ")
	print()

# # output -->
# # 1 3 5 7 9
# # 3 5 7 9 1
# # 5 7 9 1 3
# # 7 9 1 3 5
# # 9 1 3 5 7

# # pattern --> 2

for i in range(5,0,-2):
	for j in range(i,0,-1):
		print(i,end=" ")
	print()

# # output -->
# # 5 5 5 5 5
# # 3 3 3
# # 1

# # pattern --> 3

for i in range(1,10,2):
	for j in range(i,0,-2):
		print(i,end=" ")
	print()

# # output -->
# # 1
# # 3 3
# # 5 5 5
# # 7 7 7 7
# # 9 9 9 9 9

# # pattern --> 4

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


# pattern --> 5

count = 1
for i in range(1,5):
	for j in range(i):
		print(count, end=" ")
		count += 1
	print()

# output -->
# 1
# 2 3
# 4 5 6
# 7 8 9 10


# pattern --> 6

for i in range(4):
    for j in range(4):
        if(j == 3 or i == 3 or i == 0 or j == 0):
            print("@", end=" ")
        else:
            print(" ", end=" ")
    print()


# output -->
# @ @ @ @
# @     @
# @     @
# @ @ @ @


# pattern --> 7

for i in range(1,6):
	for j in range(i):
		print(i,end=" ")
	print()


# output -->
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# pattern --> 8

n = 11
for i in range(1, 6):
    for j in range(1, n-i, 2): 
        print(j, end=" ")
    n -= 1	   
    print()					 

# output -->
# 1 3 5 7 9 
# 1 3 5 7 
# 1 3 5 
# 1 3 
# 1 

# ---------------  © All copyrights reserved by Raj -------------------- #