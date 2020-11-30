'''
Week - 10 --> Programming solutions
Question 1 --> Formula
'''

import math
nums = list(map(int, input().split(',')))
ans = []

for each in nums:
    ans.append(str(round(math.sqrt((2*50*each)/30))))

print(','.join(ans), end="")

'''
Question 2 ---> word-sorting
'''

word = input().split(',')

print(','.join(sorted(word)), end="")

'''
Question 3 ---> Numbers
'''

m, n = map(int, input().split(','))
ans = []


def each_even(digit):
    while digit != 0:
        rem = digit % 10
        if rem % 2 != 0:
            return False
        digit = int(digit / 10)
    return True


for i in range(m, n+1):
    if i % 2 == 0:
        if each_even(i):
            ans.append(str(i))

print(','.join(ans), end='')
