from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)

cprint('Hello, World!', 'green', 'on_red')