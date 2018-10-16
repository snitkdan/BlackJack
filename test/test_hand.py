import unittest
from src.Hand import Hand
from src.Card import Card
from src.BinaryTree import BinaryTreeNode, BinaryTree

class TestHand(unittest.TestCase):
    """
    This class tests the Hand class
    """

    def test_empty_hand(self):
        """
        Tests the state of a newly initialized hand
        """
        h = Hand()
        self.assertListEqual(list(h.get_possible_scores()), [0])
        self.assertEqual(h.hands.root.val, 0)
        self.assertListEqual(list(h.get_cards()), [])

    def test_add_card_one_not_ace(self):
        """
        Tests the state of adding 1 non-ace card to the hand
        """
        h = Hand()
        card = Card('king', [10])
        h.add_card(card)
        self.assertListEqual(list(h.get_possible_scores()), [10])
        self.assertListEqual(list(h.get_cards()), [card])
        expected_tree = BinaryTree(BinaryTreeNode(0, BinaryTreeNode(10)))
        self.assertTrue(h.hands.is_equivalent(expected_tree))

    def test_add_card_one_ace(self):
        """
        Tests the state of adding 1 ace card to the hand
        """
        h = Hand()
        card = Card('ace', [1, 11])
        h.add_card(card)
        self.assertListEqual(list(h.get_possible_scores()), [1, 11])
        self.assertListEqual(list(h.get_cards()), [card])
        expected_tree = BinaryTree(BinaryTreeNode(0, BinaryTreeNode(1), BinaryTreeNode(11)))
        self.assertTrue(h.hands.is_equivalent(expected_tree))

    def test_add_card_multiple_no_ace(self):
        """
        Tests the state of adding multiple non-ace cards to the hand
        """
        h = Hand()
        card1 = Card('two', [2])
        card2 = Card('king', [10])
        h.add_card(card1)
        h.add_card(card2)
        self.assertListEqual(list(h.get_possible_scores()), [12])
        self.assertListEqual(list(h.get_cards()), [card1, card2])
        expected_tree = BinaryTree(BinaryTreeNode(0, BinaryTreeNode(2, BinaryTreeNode(12))))
        self.assertTrue(h.hands.is_equivalent(expected_tree))

    def test_add_card_multiple_w_ace(self):
        """
        Tests the state of adding 1 ace and 1 non-ace card to the hand
        """
        h = Hand()
        card1 = Card('ace', [1, 11])
        card2 = Card('king', [10])
        h.add_card(card1)
        h.add_card(card2)
        self.assertListEqual(list(h.get_possible_scores()), [11, 21])
        self.assertListEqual(list(h.get_cards()), [card1, card2])
        expected_tree = BinaryTree(BinaryTreeNode(0, BinaryTreeNode(1, BinaryTreeNode(11)), BinaryTreeNode(11, BinaryTreeNode(21))))
        self.assertTrue(h.hands.is_equivalent(expected_tree))

    def test_blackjack(self):
        """
        Tests whether a blackjack (21 valued hand) is correctly identified
        """
        h = Hand()
        card1 = Card('ace', [1, 11])
        card2 = Card('king', [10])
        h.add_card(card1)
        self.assertFalse(h.has_blackjack())
        h.add_card(card2)
        self.assertTrue(h.has_blackjack())

    def test_is_bust_no_ace(self):
        """
        Tests whether a bust (all possible values > 21) is correctly identified, excluding aces.
        """
        h = Hand()
        card = Card('king', [10])
        h.add_card(card)
        self.assertFalse(h.is_bust())
        h.add_card(card)
        self.assertFalse(h.is_bust())
        h.add_card(card)
        self.assertTrue(h.is_bust())

    def test_is_bust_w_ace(self):
        """
        Tests whether a bust (all possible values > 21) is correctly identified, including aces.
        """
        h = Hand()
        card1 = Card('ace', [1, 11])
        card2 = Card('king', [10])
        h.add_card(card1)
        self.assertFalse(h.is_bust())
        h.add_card(card2)
        self.assertFalse(h.is_bust())
        h.add_card(card2)
        self.assertFalse(h.is_bust())
        h.add_card(card2)
        self.assertTrue(h.is_bust())

    def test_best_score_no_ace(self):
        """
        Tests whether the correct best score is returned, excluding aces.
        """
        h = Hand()
        card = Card('king', [10])
        h.add_card(card)
        self.assertEqual(h.get_best_score(), 10)
        h.add_card(card)
        self.assertEqual(h.get_best_score(), 20)
        h.add_card(card)
        self.assertEqual(h.get_best_score(), 30)


    def test_best_score_w_ace(self):
        """
        Tests whether the correct best score is returned, including aces.
        """
        h = Hand()
        card1 = Card('ace', [1, 11])
        card2 = Card('king', [10])
        h.add_card(card1)
        self.assertEqual(h.get_best_score(), 11)
        h.add_card(card2)
        self.assertEqual(h.get_best_score(), 21)
        h.add_card(card2)
        self.assertEqual(h.get_best_score(), 21)
        h.add_card(card2)
        self.assertEqual(h.get_best_score(), 31)

    def test_get_priority_nonbust(self):
        """
        Tests whether the correct priority is assigned to non-bust hands
        """
        h = Hand()
        card1 = Card('ace', [1, 11])
        card2 = Card('king', [10])
        h.add_card(card1)
        self.assertEqual(h.get_priority(), 11)
        h.add_card(card2)
        self.assertEqual(h.get_priority(), 21)
        h.add_card(card2)
        self.assertEqual(h.get_priority(), 21)

    def test_get_priority_bust(self):
        """
        Tests whether the correct priority is assigned to busted hands
        """
        h = Hand()
        card1 = Card('ace', [1, 11])
        card2 = Card('king', [10])
        h.add_card(card1)
        self.assertEqual(h.get_priority(), 11)
        h.add_card(card2)
        self.assertEqual(h.get_priority(), 21)
        h.add_card(card2)
        self.assertEqual(h.get_priority(), 21)
        h.add_card(card2)
        self.assertEqual(h.get_priority(), -31)



