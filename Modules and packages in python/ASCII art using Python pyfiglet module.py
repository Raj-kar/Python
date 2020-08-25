import pyfiglet
from termcolor import colored, cprint
from random import choice

text = input("Input your text: ")
color = input("Enter color: ")

ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")

ASCII_text = pyfiglet.figlet_format(text)

try:
    cprint(colored(ASCII_text, color))
except BaseException:
    print("\n Available text colors:", ava_colors)
    # if user input wrong color, automatically puts a color
    cprint(colored(ASCII_text, choice(ava_colors)))


