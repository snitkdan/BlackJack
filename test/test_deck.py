import unittest
from src.Deck import Deck


class TestDeck(unittest.TestCase):
    """
    This class tests the Deck class
    """

    def test_get_suit(self):
        """
        This tests whether the correct suit is returned given different card indices
        """
        d = Deck()
        actual_suits1 = [d.get_suit(i) for i in [0, 13, 26, 39]]
        actual_suits2 = [d.get_suit(i) for i in [5, 18, 31, 44]]
        self.assertListEqual(actual_suits1, d.suits)
        self.assertListEqual(actual_suits2, d.suits)

    def test_draw_simple(self):
        """
        This tests whether the state of the deck is correctly updated following a series of draws
        """
        d = Deck()
        d.draw()
        self.assertEqual(sum(d.cards), 51)
        d.draw()
        d.draw()
        self.assertEqual(sum(d.cards), 49)
        for _, card in d.card_mapping.items():  # ensure cards remain generic
            self.assertIsNone(card.get_suit())

    def test_draw_edge(self):
        """
        This tests whether the deck can correctly be drawn from until exhaustion
        """
        d = Deck()
        curr_num_cards = 52
        while d.draw():
            curr_num_cards -= 1
            self.assertEqual(sum(d.cards), curr_num_cards)
