from random import choice
# use external module termcolor for genarate beautiful colors
from termcolor import colored, cprint
# colors avaliable for termcolor !
ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")


# decorate func. print statements with different colors
def decorate(str):
    cprint(colored(str, choice(ava_colors)))


def show_doors():
    decorate(" ********  ********  ******** ")
    decorate(" * DOOR *  * DOOR *  * DOOR * ")
    decorate(" *   1  *  *   2  *  *   3  * ")
    decorate(" ********  ********  ******** ")
    decorate("Out of three only one door has BMW, and other two door has GOAT !")