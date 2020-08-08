value = input("Enter a number to check amstrong or not :: ")

s = 0;
for i in value:
	s += int(i)**3

if s == int(value):
	print(f"{value} is amstrong number")
else:
	print(f"{value} is not a amstrong number")


