# Write a Python program to count the even, odd numbers in a given array(list) of integers using Lambda.


count = lambda *args: len([num for num in args if num % 2 == 0])

nums = [1, 2, 3, 4, 5, 6, 7]
even = count(*nums)
odd = len(nums) - even

print(f"List has {even} even numbers and {odd} numbers")

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
even = count(*array_nums)
odd = len(array_nums) - even

print(f"List has {even} even numbers and {odd} numbers")


# you may also use two different lambda function for check even and odd number !
