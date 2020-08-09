# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string


def pangrams(str):
    count = 0
    str = set(str.lower())
    for i in str:
        if i in string.ascii_lowercase[:]:
            count += 1
    return count == 26  # it's mean if count == 26 retrun True else return False


print(pangrams("The quick brown fox jumps over the lazy dog"))
print(pangrams("The Python is awesome now a days"))

# in short


def pangrams(str):
    alpha = string.ascii_lowercase[:]
    return set(alpha) <= set(str.lower())


print(pangrams("The quick brown fox jumps over the lazy dog"))
