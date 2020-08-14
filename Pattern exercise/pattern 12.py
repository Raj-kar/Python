# 123456789
#  2345678
#   34567
#    456
#     5

num = int(input("Enter a range :: "))
num += 1

for i in range(1, num):
    for j in range(1, (num*2)-2):
        if j >= i and j<= ((num*2)-2)-i:
            print(j, end="")
        else:
            print(" ", end="")
    print()
