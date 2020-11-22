value = "199"
userInput = value 

square = 1
flag = 0
prev_value = [];

while value != "1":
	s = 0
	for i in value:
		square = int(i)**2
		print(f"square of {i} = {square}")
		s += square
		print(f"sum of the square is = {s}")

	value = str(s)

	if(value in prev_value):
		print(f"\n{userInput} is not a happy Number ....  :( \n")
		flag = 1
		break
	prev_value.append(value)

if(flag == 0):
	print(f"\n{userInput} is a happy Number ....  :) :) :) \n")