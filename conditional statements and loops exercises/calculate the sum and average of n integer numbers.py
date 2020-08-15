# Write a Python program to calculate the sum and average of n integer numbers,
# (input from the user). Input 0 to finish <---

# Write a Python program to calculate the sum and average of n integer numbers,
# (input from the user). Input 0 to finish.

num = 1
s = 0
count = 0

print("Enter num [0 for exit]: ")
while num != 0:
	num = int(input())
	s += num
	count += 1


print(f"Sum of {count-1} numbers is {s} and average is {s//(count-1)}")


