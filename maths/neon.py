value = int(input("Enter a number to check neon or not :: "))

neon = value*value
s = 0;  
for i in str(neon):
	s += int(i)

if s == value:
	print(f"{value} is a neon number")
else:
	print(f"{value} is not a neon number")