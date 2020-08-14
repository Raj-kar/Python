# Write a Python program to rearrange positive and negative numbers,
# in a given array(list) using Lambda.

array_nums = [-1, 2, -3, 5, 7, 6, 9, -10]

rearrange = lambda *args : sorted([num for num in args if num > 0 ])

print(rearrange(*array_nums))