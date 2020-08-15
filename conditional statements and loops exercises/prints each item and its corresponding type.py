# Write a Python program that prints each item and its corresponding type from the following list.


datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]


for i in datalist:
    print(f"Type of {i} is {type(i)}")

    # Type of 1452 is <class 'int'>
    # Type of 11.23 is <class 'float'>
    # Type of (1+2j) is <class 'complex'>
    # Type of True is <class 'bool'>
    # Type of w3resource is <class 'str'>
    # Type of (0, -1) is <class 'tuple'>
    # Type of [5, 12] is <class 'list'>
    # Type of {'class': 'V', 'section': 'A'} is <class 'dict'>
