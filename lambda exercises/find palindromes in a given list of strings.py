# Write a Python program to find palindromes in a given list of strings using Lambda.

check_palin = lambda *args : [(val) for val in args if str(val) == str(val)[::-1]]

print("palindromes are :: ",end= " ")
print(check_palin(*["Raj","wow",121,353,"Raima","123321"]))

# if you only want to check texts, this might be a best approach

texts = ["php", "wow", "Python", "abcd", "Java", "aaa"]

check_palin = list(filter(lambda x: x == "".join(reversed(x)),texts))

print(check_palin)