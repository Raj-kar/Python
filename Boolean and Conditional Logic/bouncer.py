print("\n Enter your age for Entry ::")

age = int(input())

if age:
	if age >= 21:
		print("You're allow and also can drink ..!")
	elif age >= 18:
		print("You're allow but can't drink ..!")
	else:
		print("you are not allowed !")
else:
	print("We got No response from you ...!!")