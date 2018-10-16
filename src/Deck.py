from random import choice
from copy import deepcopy
from Card import Card


class Deck(object):
    """
    This class represents a standard 52 card deck that
    can be drawn from.
    """
    def __init__(self):
        """
        Constructs a Deck
        """
        self.cards = [1 for _ in range(52)] # [1,1,1...] where '1' in position i means card i is in the deck
        self.card_mapping = {
            0: Card('ace', [1, 11]),
            1: Card('two', [2]),
            2: Card('three', [3]),
            3: Card('four', [4]),
            4: Card('five', [5]),
            5: Card('six', [6]),
            6: Card('seven', [7]),
            7: Card('eight', [8]),
            8: Card('nine', [9]),
            9: Card('ten', [10]),
            10: Card('jack', [10]),
            11: Card('queen', [10]),
            12: Card('king', [10])
        }
        self.suits = ['diamond', 'spade', 'club', 'heart']

    def __isvalidcard(self, card_index: int):
        """
        :param card_index: index within self.cards corresponding to a card in the deck
        :return: True if 0 <= card_index < 52, and False otherwise
        """
        return card_index >= 0 and card_index < len(self.cards)

    def __getcard(self, card_index: int):
        """
        :param card_index: a valid card index (raises ValueError if invalid)
        :return: the Card corresponding to card_index
        """
        if not self.__isvalidcard(card_index):
            raise ValueError('invalid card: {0}'.format(card_index))
        return self.card_mapping[card_index % 13]

    def get_suit(self, card_index: int):
        """
        :param card_index: a valid card index (raises ValueError if invalid)
        :return: one of 'diamond', 'spade', 'club', 'heart'
        """
        if not self.__isvalidcard(card_index):
            raise ValueError('invalid card: {0}'.format(card_index))
        suit_index = 0
        while card_index >= 13:
            card_index -= 13
            suit_index += 1
        return self.suits[suit_index]

    def draw(self):
        """
        :return: a random Card drawn from the deck, which will be removed from the deck thereafter (or None if the
        deck is empty)
        """
        undrawn_cards = [i for i,v in enumerate(self.cards) if v > 0]
        if len(undrawn_cards) <= 0:
            return None
        card_index = choice(undrawn_cards)
        self.cards[card_index] -= 1  # remove card from the deck
        # return a copy of this card to be used by the client with the appropriate suit
        card = deepcopy(self.__getcard(card_index))
        card.set_suit(self.get_suit(card_index))
        return card


