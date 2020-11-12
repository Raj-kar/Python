'''
Week - 9 --> Programming solutions
Question 1 --> Palindrome
'''

name = input()

if name == ''.join(reversed(name)):
    print("YES", end="")
else:
    print("NO", end="")


'''
Question 2 ---> lexicographically smallest palindrome
'''

word = input()
length = len(word)


def SmallestPalindrome(word, length):
    i = 0
    j = length - 1
    word = list(word)  # creating a list from the input word
    while (i <= j):
        if (word[i] == word[j] == '.'):
            word[i] = word[j] = 'a'
        elif word[i] != word[j]:
            if (word[i] == '.'):
                word[i] = word[j]
            elif (word[j] == '.'):
                word[j] = word[i]
            else:  # worst case situation when palindrome condition is not met
                return -1
        i = i + 1
        j = j - 1
    return "".join(word)  # to turn the list back to a string


# Print the output of your function
print(SmallestPalindrome(word, length), end="")


'''
Question 3 ---> Holes
'''


def number_of_holes(string):
    one_hole = ['A', 'D', 'O', 'P', 'R', 'Q']
    two_hole = ['B']
    total = 0

    for each in string:
        if each in two_hole:
            total += 2
        elif each in one_hole:
            total += 1

    print(total, end="")


string = input()
number_of_holes(string.upper())
