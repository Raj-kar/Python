
s = 0  # global var


def detect_local_var():
    x = 1
    y = 2
    str1 = "Python_awesome"
    print("Python is awesome")


print(detect_local_var.__code__.co_nlocals) # for localm variables
print(detect_local_var.__code__.co_consts)  # for constant 