# Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.

# Input a dog's age in human years: 15
# The dog's age in dog's years is 73


def calculate_dog_age(age):
    s = 0
    remain_age = age - 2

    if(remain_age >= 0):
        s += 21
    else:
        s += 10.5

    if remain_age > 0:
        s += remain_age * 4

    print(f"The dog's age in dog's years is {s}")

calculate_dog_age(1)		# The dog's age in dog's years is 10.5
calculate_dog_age(2)		# The dog's age in dog's years is 21
calculate_dog_age(12)		# The dog's age in dog's years is 61
calculate_dog_age(15)		# The dog's age in dog's years is 73
