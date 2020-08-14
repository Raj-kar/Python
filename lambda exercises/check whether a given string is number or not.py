# Write a Python program to check whether a given string is number or not using Lambda

check_string = lambda string: True if string == str(string) else False


print(check_string("Raj"))

print(check_string(12))