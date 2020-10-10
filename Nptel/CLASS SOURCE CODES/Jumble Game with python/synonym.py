# the first four internal python module use to show animation to the user !
import itertools
import threading
import time
import sys
# use choice for choice a random color and a random synonyms !
from random import choice
# for print statements with colors
from termcolor import colored, cprint
# for find synonyms of the word [a external module !]
from PyDictionary import PyDictionary
dictionary = PyDictionary()

ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")


def decorate(str):  # print statements with random color !
    cprint(colored(str, choice(ava_colors)), end="")


def found_syn(word):    # found synonyms
    is_found = False    # animation will run, untill is_found is Ture

    def animate():  # animation start here !
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if is_found:
                break
            decorate(f'\rloading synonyms {c}')  # print the loading bars
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()   # start the animation !

    synonym = dictionary.synonym(word)  # find the synonyms of the word
    is_found = True     # after found stop the loading animation

    # if synonyms found return it,
    if(synonym):
        return synonym
    else:
        # otherewise return None, and print the answer !
        # if internet not connected, we can't find any synonyms !
        decorate("Check your internet connection !")
        return None
