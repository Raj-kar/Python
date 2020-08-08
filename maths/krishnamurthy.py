value = input("Enter a vlaue to check krishnamurthy number or not :: ")

fact = 1
s = 0
for i in value:
	for j in range(1,int(i)+1):
		fact *= int(j)
	s += fact
	fact = 1

if s == int(value):
	print(f"{value} is a krishnamurthy number")
else:
	print(f"{value} is not a krishnamurthy number")