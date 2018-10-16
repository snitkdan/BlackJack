import unittest
from src.Card import Card
from src.Game import Game

class TestGame(unittest.TestCase):
    """
    This class tests the Game class
    """

    def test_initialization_edge(self):
        """
        Tests the empty player list initialization edge case
        """
        try:
            g = Game([])
            self.assertIsNone(1)
        except ValueError:
            self.assertTrue(True)

    def test_singleplayer(self):
        """
        Tests a simple single-player game of blackjack
        """
        g = Game(['bob'])
        ace = Card('ace', [1, 11])
        king = Card('king', [10])
        self.assertTrue(g.hit(ace))
        self.assertTrue(g.hit(king))
        g.stay()
        winner = g.get_winner()
        self.assertEqual(winner, 'bob')

    def test_multiplayer_nonbust(self):
        """
        Tests a simple two-player game of blackjack where both players stay
        """
        g = Game(['bob', 'jane'])
        ace = Card('ace', [1, 11])
        king = Card('king', [10])
        self.assertTrue(g.hit(ace))
        self.assertTrue(g.hit(king))
        g.stay()
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(king))
        g.stay()
        winner = g.get_winner()
        self.assertEqual(winner, 'bob')

    def test_multiplayer_bust(self):
        """
        Tests a simple two-player game of blackjack where one player busts and the other stays
        """
        g = Game(['bob', 'jane'])
        ace = Card('ace', [1, 11])
        king = Card('king', [10])
        self.assertTrue(g.hit(ace))
        self.assertTrue(g.hit(king))
        g.stay()
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(king))
        self.assertFalse(g.hit(king))
        winner = g.get_winner()
        self.assertEqual(winner, 'bob')

    def test_multiplayer_rankings_complex(self):
        """
        Tests a complex multi-player game of blackjack in which some players bust,
        some do not, verifying that the final ranking is correctly ordered.
        """
        g = Game(['bob', 'jane', 'joe', 'katy'])
        ace = Card('ace', [1, 11])
        king = Card('king', [10])
        five = Card('five', [5])
        # bob --> bust w/ 25
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(king))
        self.assertFalse(g.hit(five))
        # jane --> stay w/ 15
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(five))
        g.stay()
        # joe --> stay w/ 20
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(king))
        g.stay()
        # katy --> stay w/ 21
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(king))
        self.assertTrue(g.hit(ace))
        g.stay()
        # get the winner
        self.assertListEqual(g.get_rankings(), ['katy', 'joe', 'jane', 'bob'])


