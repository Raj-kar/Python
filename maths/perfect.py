value = input("Enter a number to check perfect number or not :: ")

s = 0

for i in range(1,int(value)):
	if int(value) % i == 0:
		s += i

if s == int(value):
	print(f"{value} is a perfect number")
else:
	print(f"{value} is not a perfect number")


# 496,8128,28,6 are perfect numbers because sum of the factors of these number are equal to the num.
# as example 6 factors are 1,2,3[exclutive 6], so 1+2+3 = 6 same as 28..so on.