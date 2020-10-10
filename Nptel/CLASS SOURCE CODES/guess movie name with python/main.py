import random
movies = ['tanhaji', 'malang', 'junglebook', 'titanic',
          'chhapaak', 'thappad', 'panga', 'hacked', 'dhoom', 'lootcase']

s_movie = random.choice(movies)
length = len(s_movie)
point = 10
dashes = ['_'] * length


def calculate_point():
    global point
    if point > 0:
        point -= 1


def get_hint(letter, start=0, add=0):
    movie = list(s_movie)
    try:
        indx = movie[start:].index(letter) + add
    except:
        decorate(f"Movie has no letter {letter}")
    else:
        if dashes[indx] == '_':
            dashes[indx] = letter
        else:
            get_hint(letter, start=indx + 1, add=indx + 1)
        decorate(*dashes)


def start():
    decorate(f"Guess the movie name, [the movie has {length} letters] :  ")
    decorate(*dashes)
    while ''.join(dashes) != s_movie:
        answer = input(
            "Enter any letter, to get some hint ! or, Enter the movie name  ").lower()
        if answer == s_movie:
            decorate("CORRECT !")
            break
        else:
            calculate_point()
            get_hint(answer)
    decorate(f"Your total point is = {point}")


start()
