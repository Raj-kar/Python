import unittest

from card import Card
from deck import Deck


class TestCard(unittest.TestCase):
    def setUp(self):
        self.c1 = Card("A", "Hearts")

    def test_init(self):
        """test card name and suit"""
        self.assertEqual(self.c1.value, 'A')
        self.assertEqual(self.c1.suit, 'Hearts')
        with self.assertRaises(AttributeError):
            self.c1.marks

    def test_repr(self):
        """test repr of card !"""
        self.assertEqual(repr(self.c1), "A of Hearts")


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.d1 = Deck()

    def test_init(self):
    	""" decks should be card attribute, has 52 cards """
    	self.assertTrue(isinstance(self.d1.cards, list))
    	self.assertEqual(len(self.d1.cards), 52)

    def test_repr(self):
    	""" test repr of duck !"""
    	self.assertEqual(repr(self.d1), "Deck of 52 cards")

    def test_count(self):
    	""" count how many card left has deck """
    	self.assertEqual(self.d1.count(), 52)
    	self.d1.cards.pop()
    	self.assertEqual(self.d1.count(), 51)

    def test_deal_sufficient_card(self):
    	""" check sufficient card has on the deck """
    	self.assertEqual(len(self.d1._deal(10)), 10)
    	self.assertEqual(len(self.d1._deal(42)), 42)

    def test_deal_insufficient_card(self):
    	""" check insufficient card has on the deck """
    	self.assertEqual(len(self.d1._deal(100)), 52)
    	with self.assertRaises(ValueError):
    		self.d1._deal(52)
    	self.assertEqual(len(self.d1.cards), 0)

    def test_deal_cards(self):
    	"""test deal cards with the last card"""
    	last_card = self.d1.cards[-1]
    	deal_card = self.d1.deal_card()
    	self.assertEqual(last_card, deal_card)
    	self.assertEqual(self.d1.count(), 51)

    def test_deal_hand(self):
    	"""test deal hand with removing cards"""
    	self.assertEqual(len(self.d1.deal_hand(52)), 52)
    	with self.assertRaises(ValueError):
    		self.d1.deal_hand(10)

    def test_shuffle_with_full_deck(self):
    	cards = self.d1.cards[:]
    	self.d1.shuffle()
    	self.assertNotEqual(cards, self.d1.cards)
    	self.assertEqual(len(cards),len(self.d1.cards))

    def test_shuffle_with_no_full_deck(self):
    	self.d1._deal(1)
    	with self.assertRaises(ValueError):
    		self.d1.shuffle()


if __name__ == "__main__":
    unittest.main()
