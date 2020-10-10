from functions import decorate, ascii_text


def rules():    # Some Game rules, first shown at screen !
    decorate(" ************************************************************ ")
    decorate(" *                                                          * ")
    decorate(" *     Welcome to Word jumbling, Suffle, re-arange Game!    * ")
    decorate(" *                                                          * ")
    decorate(" ************************************************************ ")
    decorate("Game Rules --->> Two-player game | Each time a player enters a word and the game shows the word in shuffle form.")
    decorate(
        "Then player 2 will guess it. If the correct, then player 2 enter a word, and player 1 will guess it !")
    decorate(
        "Both the player will get three hints, one each time if they can't answer the word at once ..!")
    decorate("The Game will run, untill player exit it !")


def loading_screen(p1, p2):     # welcome player 1 and 2
    ascii_text(f"WELCOME  {p1} and  {p2}")
    decorate(f"We start with {p1} turn ..!")
    decorate("Don't show the word to your opponent !")

# -> decorate is a function which you find at functions.py file
# -> It's just like print function, but it prints statements with different colors !
