# import random
from random import randint

print("..... rock .....\n..... paper .....\n..... scissors .....")

user1= input("Enter player 1's Choice :: ").lower()
# user1 = user1.lower()

# rand_num=random.randint(0,2)
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
		print("player 1 WIN")
	elif(user1 == "paper" and comp=="rock"):
		print("player 1 WIN")
	elif(user1 == "scissors" and comp=="paper"):
		print("player 1 WIN")
	elif(user1 == comp):
		print("It's a Tie")
	else:
		print("Computer WIN")
else:
	print("Wrong Input ...!")