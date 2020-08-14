# Write a Python program to add two given lists using map and lambda.

add_list = lambda a, b: list(map(lambda x,y: x+y ,a,b))

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

print(add_list(nums1,nums2))