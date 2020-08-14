

starts_with = lambda string: print(
    "True") if string.startswith("p") else print("False")


starts_with("python")  # True
starts_with("java")		# False
starts_with("Python")  # False, because here we input capital "P"

# modify the function ..!


starts_with= lambda string: print("True") if (
    string.lower()).startswith("p") else print("False")


# True , we use.lower() function for convert the input capital to normal :)
starts_with("Python")
starts_with("Java")		# False
