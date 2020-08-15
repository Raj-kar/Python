#     5
#    456
#   34567
#  2345678
# 123456789



num = int(input("Enter a range :: "))
num += 1

for i in range(1, num):
    for j in range(1, (num*2)-2):
        if j >= num-i and j<= (num-2)+i:
            print(j, end="")
        else:
            print(" ", end="")
    print()
