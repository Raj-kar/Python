from random import randint

user_score = 0
comp_score = 0

user_round = input("\nHow many Round you want to play ? ")
user_round = int(user_round)

count = 0
while count < user_round:
    print("\n..... rock .....\n..... paper .....\n..... scissors .....")
    print("*** Press  q  anyTime for quit the Game ::")

    user1 = input("\nEnter your Choice :: ").lower()

    if user1 == "q":
        break

    rand_num = randint(0, 2)

    if rand_num == 0:
        comp = "rock"
    elif rand_num == 1:
        comp = "paper"
    elif rand_num == 2:
        comp = "scissors"

    print(f"Computer choose :: {comp}")

    if user1 == "paper" or user1 == "rock" or user1 == "scissors":
        if user1 == "rock" and comp == "scissors":
            print("\nplayer 1 WIN")
            user_score += 1
            print(f"\nplayer 1 score = {user_score} and computer score = {comp_score}")
        elif user1 == "paper" and comp == "rock":
            print("\nplayer 1 WIN")
            user_score += 1
            print(f"\nplayer 1 score = {user_score} and computer score = {comp_score}")
        elif user1 == "scissors" and comp == "paper":
            print("\nplayer 1 WIN")
            user_score += 1
            print(f"\nplayer 1 score = {user_score} and computer score = {comp_score}")
        elif user1 == comp:
            print("\nIt's a Tie")
            print(f"\nplayer 1 score = {user_score} and computer score = {comp_score}")
        else:
            print("\nComputer WIN")
            comp_score += 1
            print(f"\nplayer 1 score = {user_score} and computer score = {comp_score}")

    else:
        print("\nEnter a valid move ...!")

    count += 1

print("\n******* Final Result *********")
if user_score > comp_score:
    print("\nPlayer 1 Win ... :)")
elif user_score == comp_score:
    print("\nIt's a tie match !!.. Try agin Next Time ;)")
else:
    print("\nOps ..! Computer win  :( ")
