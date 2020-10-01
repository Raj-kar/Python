# pattern --> 1

for i in range(1,10,2):
	for j in range(i,i+9,2):
		print(j%10,end='')
	print()

# output -->
# 1 3 5 7 9
# 3 5 7 9 1
# 5 7 9 1 3
# 7 9 1 3 5
# 9 1 3 5 7

# pattern --> 2

word = "ABCDEF"

for i in range(len(word), 0, -1):
    for j in range(0, i):
    	print(word[j],end="")
    print()

# < -----Using-----Slice--------- > #

print(word)
for i in range(1, len(word)):
	print(word[:-i])

# output -->
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A

# pattern --> 3

for i in range(1,6):
	num = 9
	for k in range(5,i,-1):
		print(" ",end="")
	for j in range(i):
		print(num,end="")
		num -= 2
	print()

# output -->
#     9
#    97
#   975
#  9753
# 97531


# pattern --> 4

for i in range(1,10,2):
	c = 1
	for j in range(1,10,2):
		if i+j <= 10:
			print(j,end='')
		else:
			print(c,end='')
			c+=2
	print()

# output -->
# 1 3 5 7 9
# 1 3 5 7 1
# 1 3 5 1 3
# 1 3 1 3 5
# 1 1 3 5 7

# pattern --> 5

space = 4
for i in range(9, 0, -2):
    for k in range(space):
        print(" ",end="")
    for j in range(i, 10, 2):
        print(j, end="")
    print()
    space -= 1

# output -->
#     9
#    79
#   579
#  3579
# 13579

# ---------------  © All copyrights reserved by Raj -------------------- #
