import requests
from termcolor import cprint, colored
from random import choice


url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}
ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")

while True:
    try:
        input("\n ---- Press Enter ----- \n")
        response = requests.get(url, headers=headers).json()
        # {"Accept" : "text/palin"} for the plain text !

        cprint(colored(response['joke'], choice(ava_colors)))
    except:
        cprint(colored("Opps ! something went wrong ","red"))
        break
