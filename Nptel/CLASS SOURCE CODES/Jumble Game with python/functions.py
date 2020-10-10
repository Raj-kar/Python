# shuffle can randomly shuffles a list, and choice make a choice from a set of different items !
from random import choice, shuffle
# use external module termcolor for genarate beautiful colors
from termcolor import colored, cprint
# using pyfiglet, external module -> we can draw ascii_art very easily !
import pyfiglet
# found_syn function return us synonyms of the word which player enter ! [check synonym.py]
from synonym import found_syn

# colors avaliable for termcolor !
ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")


# decorate func. print statements with different colors
def decorate(str):
    cprint(colored(str, choice(ava_colors)))


# ascii_text func. print statements with ascii_art
def ascii_text(str):
    text = pyfiglet.figlet_format(str)
    decorate(text)          # print ascii_art with color


# jumble func. shffle the given word
def jumble(word):
    # shuffle can only shuffle list, so make the word list, using inbuild list method
    jumble_word = list(word)
    # shuffle the list of letters
    shuffle(jumble_word)
    # join back the letters using inbuild join method !
    shuffle_word = ''.join(jumble_word)

    # after suffling is the word is same is as given word again shuffle it, else return it !
    if(word != shuffle_word):
        return shuffle_word
    else:
        jumble(word)


# display hint msg --> create this to keep our code DRY [Don't repeate yourself !]
def give_hint(hintMsg, hint, word, join="with"):
    decorate(f"\n The word {hintMsg} {join} {hint}")
    answer = input().lower()
    # if after hint player guess it correctly, return True and print CORRECT, and going to next player
    if(answer == word):
        return True


# show 3 hint to the player !
def get_hint(word):
    decorate("Hint ---> ")
    while(True):
        # 1st hint only shows the first letter of the word
        if(give_hint("starts", word[0], word)):
            return True
        # 2nd hint only shows the last letter of the word
        elif(give_hint("ends", word[len(word) - 1], word)):
            return True
        else:
            # 3rd hint shows one nearest meaning[synonyms] of the of the word
            # found_syn func, found a synonym and return it !   [check synonym.py]
            synonym = found_syn(word)
            # if found a synonym show to the user
            if(synonym):
                if(give_hint("synonyms", choice(synonym), word, "is")):
                    # after showing synonym if user guess it correctly, show CORRECT
                    return True
                # else show the original answer to the player !
                else:
                    print()  # for give one line space !
        break
