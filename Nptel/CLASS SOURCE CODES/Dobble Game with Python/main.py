import random


class Dobble_Game:
    def __init__(self, item_count):
        self.words = ['goon', 'loser',  'criminal', 'carbon',  'collection',  'helpless',  'crisis', 'adventure', 'bloodsport',
                      'pulse', 'eternal', 'swarm', 'illegal', 'hospital', 'zipper', 'devices', 'atonement', 'port', 'anxiety',
                      'allotment', 'southern', 'beyond', 'burn', 'concussion', 'branch', 'orb', 'firecracker', 'herd',
                      'graveyard', 'homeless', 'acidic', 'liqueur', 'crasher', 'piece', 'wreckage', 'settler', 'signal',
                      'circuitry', 'boulevard', 'derelict', 'pimp', 'chart', 'glacial', 'bloodstain', 'formal', 'halloweenedge',
                      'commando', 'drugstore', 'raster', 'flowers', 'fuzzy', 'founder', 'growl', 'concave', 'fizz']
        self.list1 = [] * item_count
        self.list2 = [] * item_count
        self.item_count = item_count
        self.removed_words = []

    def reset(self):
        self.list1.clear()
        self.list2.clear()
        self.words.extend(self.removed_words)
        self.removed_words.clear()
        new_count = int(input("How many items you want to add ?"))
        self.item_count = new_count

    def restart_game(self):
        choice = input("Play agin ?? [yes/no] ")
        if choice[0] == "y":
            self.reset()
            self.start()
        else:
            decorate("Thanks for playing !")

    def check_answer(self, s_word):
        answer = input("Spot the Similar Word --> ")
        if answer == s_word:
            decorate("CORRECT ..! ")
        else:
            decorate(f"Opps! the similar word is {s_word}")

        self.restart_game()

    def random_index(self, end):
        return random.randint(0, end)

    def random_word(self):
        rand_index = self.random_index(len(self.words)-1)
        rand_word = self.words[rand_index]
        self.words.remove(rand_word)
        self.removed_words.append(rand_word)
        return rand_word

    def insert_similar(self):
        s_word = self.random_word()
        length = self.item_count-1
        self.list1[self.random_index(length)] = s_word
        self.list2[self.random_index(length)] = s_word
        return s_word

    def insert_word(self, data):
        data.append(self.random_word())

    def start(self):
        while len(self.list1) < self.item_count:
            self.insert_word(self.list1)
            self.insert_word(self.list2)
        similar_word = self.insert_similar()

        decorate(self.list1)
        decorate(self.list2)

        self.check_answer(similar_word)


d_game = Dobble_Game(5)
d_game.start()