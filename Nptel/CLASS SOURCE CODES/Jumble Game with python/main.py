from design import rules, loading_screen
from functions import jumble, decorate, ascii_text, get_hint
import getpass  # use getpass for hide user input

# Program starts from home_page() [at bottom !]


def check_answer(word, answer):
    string = "C O R R E C T "
    if(word == answer):
        # if player  guess correctly, its shows correct, and then --> player 2 enter a word
        # check functions.py if you want to details on ascii_text func.
        ascii_text(string)
    else:
        # if player guess it wrong, we'll show the player 3 hints
        if(get_hint(word)):  # go to functions.py for show get_hint func.
            ascii_text(string)
            # if get_hit returns true, PRINT CORRECT
        else:
            # else print the correct word after 3 hint
            decorate(f"The correct word is ** {word} **")


def game(p1, p2):       # make game function to keep our code dry
    # PLayer 1 Enter a word
    decorate(f"{p1} Write a word : ")
    # using getpass, ** HIDE THE ENTERED WORD **  FROM PLAYER 2
    word = getpass.getpass("--> ").lower()
    # print the shuffle word --> jumble function shuffle the word [check functions.py]
    decorate(f"The Shuffled word is = {jumble(word)}")
    # ask player 2 to guess the word
    decorate(f"{p2} Enter your answer :: ")
    # take the input at answer variable
    answer = input().lower()
    # pass the both word and answer to check answer func, for check the answer !
    check_answer(word, answer)


def start_game(p1, p2):     # game will run untill user type no !
    while True:
        # call game function for player 1 -->and pass player 1 and 2 info
        game(p1, p2)
        # call game function for player 1 -->and pass player 2 and 2 info
        game(p2, p1)
        # ask player for play again? if yes the i'll start again, else end game !
        choice = input("Are you want to play again ? [yes/no] ").lower()

        if choice[0] == 'n':    # check the choice [only first char]
            decorate("Thanks for do the BETA testing ..!")
            break


def player_info():      # take player 1 and player 2 names !
    # input validation will be added !
    decorate("Enter player 1 name :: ")
    player1 = input()
    decorate("Enter player 2 name :: ")
    player2 = input()
    # pass the data to loading_screen for shown a welcome msg.[design.py]
    loading_screen(player1, player2)
    start_game(player1, player2)            # here the main game started !


def home_page():
    rules()          # go to design.py
    player_info()    # look at the upper func !


home_page()  # --> start here !
