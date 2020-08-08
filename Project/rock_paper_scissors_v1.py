print("..... rock .....\n..... paper .....\n..... scissors .....")

user1= input("Enter player 1's Choice :: ")

print("************DON'T CHEAT**************\n\n"*30)

user2= input("Enter player 2's Choice :: ")

# if (user1 == "paper" or user1 == "rock" or user1 == "scissors") and (user2 == "paper" or user2 == "rock" or user2 == "scissors"):
# 	if(user1== "rock" and user2=="scissors"):
# 		print("player 1 WIN")
# 	elif(user1 == "paper" and user2=="rock"):
# 		print("player 1 WIN")
# 	elif(user1 == "scissors" and user2=="paper"):
# 		print("player 1 WIN")
# 	elif(user1 == user2):
# 		print("DRAW")
# 	else:
# 		print("player 2 WIN")
# else:
# 	print("Wrong Input ...!")


if user1 and user2:
	if user1 == user2:
		print("It's a Tie")
	elif user1 == "paper":
		if user2 == "rock": 
			print("player 1 win")
		else:
			print("player 2 win")
	elif user1 == "rock":
		if user2 == "scissors":
			print("player 1 win")
		else:
			print("player 2 win")
	elif user1 == "scissors":
		if user2 == "paper":
			print("player 1 win")
		else:
			print("player 2 win")
	else:
		print("something went Wrong ..!")
else:
	print("We can't Hear you")




