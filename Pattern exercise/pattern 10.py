# 12345
#  2345
#   345
#    45
#     5

num = int(input("Enter a range :: "))
num += 1

for i in range(1, num):
    for j in range(1, num):
        if j >= i:
            print(j, end="")
        else:
            print(" ", end="")
    print()
