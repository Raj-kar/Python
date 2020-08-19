x = y = z = 0  # good practice

x = float(input("enter : "))
y = float(input("enter : "))
z = float(input("enter : "))
max = x

if y>max:
	max = y
if z > max:
	max = z

print(max)