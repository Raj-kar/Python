import random


# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


c1 = Card("A", "Hearts")
c2 = Card("5", "Clubs")
c3 = Card("9", "Diamond")


# print(c1)
# print(c2)
# print(c3)

# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card . Deck  should have an
# instance method called count  which returns a count of how many cards remain in the deck. Deck 's __repr__  method
# should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards",
# etc.) Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards
# from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are
# no cards left, this method should return a ValueError  with the message "All cards have been dealt". Deck  should
# have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from
# the deck, this method should return a ValueError  with the message "Only full decks can be shuffled". Deck  should
# have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck. Deck
# should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list
# of cards from the deck.


class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

        # print(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        actual = min(count, number)

        if count:
            cards = self.cards[-actual:]
            self.cards = self.cards[:-actual]
            return cards
        else:
            raise ValueError("All cards have been dealt")

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
            return "Card shuffled !"
        else:
            raise ValueError("Only full decks can be shuffled")


d = Deck()

print(d.count())

# print(d._deal(5))

# print(d.count())

# print(d.shuffle())

# print(d.cards)

d.shuffle()

print(d.deal_card())

print(d.deal_hand(5))

print(d.count())
