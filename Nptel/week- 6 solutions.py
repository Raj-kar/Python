'''
Week - 6 --> Programming solutions
Question 1 --> Remove Dublicate elements
'''

# L = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]     for test
import math
L = input()
arr = []

for each in L:
    if each not in arr and each != " ":
        arr.append(each)

print(arr, end="")

'''
Question 2 -->  Number is a power of 2 or not
'''


def isPowerOfTwo(n):
    if (n == 0):
        return "NO"
    while (n != 1):
      if (n % 2 != 0):
      	return "NO"
      n = n // 2

    return "YES"

n = int(input())

print(isPowerOfTwo(n),end="")


'''
Different approatch <- question no 2
Contribute by - @mits
'''
def Log2(x):
    if x == 0:
        return false

    return (math.log10(x) /
            math.log10(2))


def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))


n = int(input())

if(isPowerOfTwo(n)):
    print("YES", end="")
else:
    print("NO", end="")


'''
Question 3 -->  lower triangular matrix
Basic implementation ! Optimized uploaded sooooon :)
'''
num = int(input())
count = 0
arr = []


def push_values(count, values):
    values = values.split(" ")
    arr.append([])
    for each in values:
        arr[count].append(int(each))


def take_input(count):
    values = input()
    push_values(count, values)


while count < num:
    take_input(count)
    count += 1

answer = []
for i in range(num):
    answer.append([])
    for j in range(num):
        if j < i + 1:
            answer[i].append(arr[i][j])
        else:
            answer[i].append(0)

for row in answer:
    print(* row)