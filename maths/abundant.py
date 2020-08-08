value = input("Enter a number to check abundant number or not :: ")

s = 0

for i in range(1,int(value)):
	if int(value) % i == 0:
		s += i

if s > int(value):
	print(f"{value} is a abundant number..!")
	print(f"The abundant is = {s-int(value)}")
else:
	print(f"{value} is not a abundant number ..!")

# In number theory, an abundant number or excessive number is a number for which the sum 
# of its proper divisors is greater than the number itself. The integer 12 is the first abundant
# number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16. The amount by which the
# sum exceeds the number is the abundance. The number 12 has an abundance of 4(1+2+3+4 = 16)[16-12],
# for example... some abundant numbers are 12,18,21 ..!