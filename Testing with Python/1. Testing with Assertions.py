def sum_positive_nums(num1, num2):
    assert num1 > 0 and num2 > 0, "Only positive numbers allowed"
    return num1 + num2


print(sum_positive_nums(2, 2))  # 4
print(sum_positive_nums(2, -2))  # AssertionError: Only positive numbers allowed


# We can bypass assertion test with -O [like python -O Testing with Assertions.py]
# -O , stands for optimise

# Another example of assertion test


def junk_food(name):
    name = name.lower()
    assert name in ("pizza", "momo", "burger", "ice creme", "pasta", ",maggi"), "only Junk food allowed !"
    return f"Um Um, Too much tasty {name}"


print(junk_food("pizza"))  # Um Um, Too much tasty pizza
print(junk_food("Burger"))  # Um Um, Too much tasty pizza
print(junk_food("rice"))  # AssertionError: only Junk food allowed !

# Make Note :-  In assertion if it's true, it's return none and if it's false it's return assertion error
