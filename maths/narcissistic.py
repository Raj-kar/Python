value = input("Enter a number to check narcissistic number or not :: ")

v_len = len(value)
s = 0

for i in value:
	s += int(i)**v_len

if s == int(value):
	print(f"{value} is a narcissistic number")
else:
	print(f"{value} is not a narcissistic number")


# example 153 == 1^3+5^3+3^3 ,9474 == 9^4 3^4 7^4 4^4  [power will be the length of number]