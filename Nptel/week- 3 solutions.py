# <------ solution programming assignment 1 -------> #
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

print((s1 + s2 + s3 + s4 + s5) / 5, end="")

# <------ solution programming assignment 2 -------> #
list_1 = []
for i in range(1, 51):
    list_1.append(i)

a, b = input().split()
a = int(a)
b = int(b)

new_list = list_1[a:b]
for i in new_list:
    print(i)

# <------ solution programming assignment 3 -------> #
list_1 = []
for i in range(1, 51):
    list_1.append(i)

num = int(input())

count = 0
list_1 = list_1[num:]
for i in list_1:
    if i % num == 0:
        count += 1

print(count, end="")

# <-------- For Practice purpose only < Raj™ /> --------------> #
