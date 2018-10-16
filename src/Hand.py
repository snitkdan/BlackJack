from collections import deque
from BinaryTree import BinaryTree, BinaryTreeNode
from Card import Card


class Hand(object):
    """
    This class represents a Black Jack Hand (collection of cards), managing the
    score(s) associated with it, and providing methods for checking on the state of the
    hand within a standard game of Black Jack. If a name is associated with this hand, then the
    hand is being "played" by said person.
    """
    def __init__(self, name=None):
        """
        Constructs a 0 card hand
        """
        self.name = name
        self.hands: BinaryTree = BinaryTree(BinaryTreeNode(0))  # The root of the BinaryTree represents an "empty" hand
        self.cards: [Card] = deque()  # each individual card in the hand
        self.possible_scores = deque()  # can be multiple different scores due to aces double value possibilities
        self.has_non_bust = True  # if at least possible scoring is <= 21

    def get_name(self):
        """
        :return: the name of the owner of this hand
        """
        return self.name

    def add_card(self, card: Card):
        """
        Adds the given card to the current hand and recalculates the possible scores
        given this new addition.

        :param card: a Card from a standard deck (e.g. ace)
        """
        self.cards.append(card)  # maintain the card for future reference
        self.possible_scores.clear()  # clear past scores
        leaves = self.hands.get_leaves() # get the most recent scores at play
        has_non_bust = False
        for leaf in leaves:
            for i, val in enumerate(card.get_values()):  # go through each possible value of this card
                possible_score = leaf.val + val
                # each branch of the BinaryTree is a possible value of the current hand
                if i == 0:
                    leaf.left = BinaryTreeNode(possible_score)
                else:
                    leaf.right = BinaryTreeNode(possible_score)
                has_non_bust = has_non_bust or possible_score <= 21  # bust is greater than 21
                self.possible_scores.append(possible_score)
            self.has_non_bust = has_non_bust

    def get_most_recent_card(self):
        """
        :return: the most recently added card to the hand (raises ValueError of the hand is empty)
        """
        if len(self.get_cards()) < 1:
            raise ValueError('Cannot get most recent card of empty hand')
        cards = self.get_cards()
        return cards[len(cards) - 1]

    def get_cards(self):
        """
        :return: the collection of cards that make up this hand currently
        """
        return self.cards

    def get_possible_scores(self):
        """
        :return: the possible scores (as defined by standard Black Jack) for the
        current hand (0 if the hand is empty)
        """
        if len(self.possible_scores) < 1:
            return deque([0])
        return self.possible_scores

    def has_blackjack(self):
        """
        :return: True if one of the possible hands is "21", and False otherwise
        """
        return 21 in self.get_possible_scores()

    def is_bust(self):
        """
        :return: True if the only hands possible are > 21, and False otherwise
        """
        return not self.has_non_bust

    def get_best_score(self):
        """
        :return: the best possible scores (as defined by standard Black Jack) for the
        current hand (0 if the hand is empty).

        If bust, returns the lowest possible busted score. If non-bust, returns the
        highest possible non-bust.
        """
        scores = self.get_possible_scores()
        if self.is_bust():
            return min(scores)
        non_bust_scores = filter(lambda x: x <= 21, scores)
        return max(non_bust_scores)

    def get_priority(self):
        """
        :return: the value of the hand ordered from non-bust --> bust.
        If non-bust, returns the absolute value of the hand, where higher is greater priority
        If bust, returns the negative value of the hand, where higher magnitude negative is lower priority
        """
        best_score = self.get_best_score()
        return -best_score if self.is_bust() else best_score
