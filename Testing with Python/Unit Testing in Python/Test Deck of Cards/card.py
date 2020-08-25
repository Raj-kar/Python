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