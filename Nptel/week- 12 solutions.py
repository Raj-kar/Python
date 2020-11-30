'''
Week - 12 --> Programming solutions
Question 1 --> Sentence
'''

import string
line = int(input())
count = 0

while(count < line):
    sen = input()
    print(sen.upper())

'''
Question 2 ---> Letters
'''


sen = input()
special_char = []
special_char.extend(string.punctuation)

for each in sen:
    if each in special_char or each == " ":
        sen = sen.replace(each, "")

lower = 0
upper = 0

for each in sen:
    if each == each.capitalize():
        upper += 1
    else:
        lower += 1

print(upper, lower)

'''
Question 3 ---> Email ID
'''

email = input()

p1 = email.index('@')
p2 = email.index('.')

print(email[p1+1:p2], end="")
