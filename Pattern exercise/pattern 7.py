# *************
# ****** ******
# *****   *****
# ****     ****
# ***       ***
# **         **
# *           *

num = int(input("Enter a range :: "))
symbol = input("Enter a symbol :: ")	# user can enter any symbol for print !
num += 1

for i in range(1, num):
    for j in range(1, (num*2)-2):
        if j <= num-i or j >= (num-2)+i:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()
