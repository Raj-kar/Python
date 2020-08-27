import requests
from termcolor import cprint, colored
from random import choice
import pyfiglet

headers = {"Accept": "application/json"}
ava_colors = ("red", "blue", "green", "yellow", "blue", "magenta", "cyan")

ASCII_text = pyfiglet.figlet_format("DAD JOKE 3000 ")
cprint(colored(ASCII_text, choice(ava_colors)))

try:
    topic = input("\n Let tell you a joke ! Give me a topic: ")
    url = "https://icanhazdadjoke.com/search"
    params = {"term": topic}

    response = requests.get(url, headers=headers, params=params).json()

    if response['total_jokes'] > 0:
        print(
            f"\n I have got {response['total_jokes']} jokes about {topic}. Here's one:")
        print("\n", choice(response['results'])['joke'])
    else:
        cprint(colored("No ! Joke Foound ", "red"))
except Exception:
    cprint(colored("Opps ! check your network ", "red"))
