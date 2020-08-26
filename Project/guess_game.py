import random

rand = random.randint(1, 10)

while True:
    user_answer = input("\nGuess a number between 1 to 10:: ")
    user_answer = int(user_answer)

    if user_answer > rand:
        print("you are too high")
    elif user_answer < rand:
        print("you are too low")
    else:
        print("you win ..! your Guess is correct")

        user_choice = input("\nDo you want to keep playing (y/n) ")

        if user_choice == "y":
            rand = random.randint(1, 10)
        else:
            print("\nThanks For Play with Us ..!")
            break
