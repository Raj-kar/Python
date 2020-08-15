# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


add = lambda a,b : 20 if a+b >=15 and a+b <=20 else a+b


print(add(5, 4))		# 9 	

print(add(15, 4))		# 20
	
print(add(14, 3))		# 20

print(add(15, 7))		# 22