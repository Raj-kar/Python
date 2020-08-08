from random import randint


while True:
	print("\n..... rock .....\n..... paper .....\n..... scissors .....")

	user1= input("\nEnter player 1's Choice :: ").lower()

	rand_num=randint(0,2)

	if(rand_num==0):
		comp="rock"
	elif(rand_num == 1):
		comp="paper"
	elif(rand_num == 2):
		comp="scissors"

	print(f"Computer choose :: {comp}")

	if (user1 == "paper" or user1 == "rock" or user1 == "scissors"):
		if(user1== "rock" and comp=="scissors"):
			print("\nplayer 1 WIN")
		elif(user1 == "paper" and comp=="rock"):
			print("\nplayer 1 WIN")
		elif(user1 == "scissors" and comp=="paper"):
			print("\nplayer 1 WIN")
		elif(user1 == comp):
			print("\nIt's a Tie")
		else:
			print("\nComputer WIN")
	else:
		print("\nWrong Input ...!")

	user_choice=input("\nDo you want to play Again ? (y/n) ")
	if(user_choice == "y"):
		pass
	else:
		print("\nThanks for playing with us ... ;)")
		break

	