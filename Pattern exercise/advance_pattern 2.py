# pattern --> 1

for i in range(1, 10, 2):
    for j in range(i, 10, 2):
        print(j, end=" ")
    for k in range(1, i, 2):
        print(k, end=" ")
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

for i in range(10, 1, -2):
    for j in range(1, i, 2):
        print(j, end=" ")
    for k in range(1, 11 - i, 2):
        print(k, end=" ")
    print()

# output -->
# 1 3 5 7 9
# 1 3 5 7 1
# 1 3 5 1 3
# 1 3 1 3 5
# 1 1 3 5 7

# ---------------  © All copyrights reserved by Raj -------------------- #