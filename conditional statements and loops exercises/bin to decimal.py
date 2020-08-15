# Write a Python program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and print the numbers that are divisible by 5 in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001


items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)  # convert the number into decimal !

    if not x % 5:
        items.append(p)
print(','.join(items))

# 1010 [output]
