from doors import show_doors, decorate
from random import randint

doors = [0] * 3


def restart():
    choice = input("Are you want to play again ? [yes/ no] ").lower()
    if choice[0] == 'y':
        play()


def check_answer(choice, door_number):
    if (choice - 1) == door_number:
        decorate("CORRECT !")
    else:
        re_choice = int(
            input("Are you want to change your choice ?[1/2/3] :  "))
        if (re_choice - 1) == door_number:
            decorate("CORRECT !")
        else:
            decorate(f"BMW has on door number {door_number + 1}")
    restart()


def push_goats():
    for i in range(3):
        if not doors[i]:
            doors[i] = 'Goat'


def push_gift():
    rand = randint(0, 2)
    doors[rand] = "BMW"
    push_goats()
    return rand


def play():
    show_doors()
    door_number = push_gift()
    choice = int(input("Select any one door [1/2/3] :  "))
    check_answer(choice, door_number)


play()
