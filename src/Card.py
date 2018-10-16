class Card(object):
    """
    This class represents a standard playing card (e.g. Ace) as it
    is represented in a game of Black Jack.
    """
    def __init__(self, name: str, values: [int], suit=None):
        """
        :param name: the title of the card (e.g. king)
        :param values: the values this card takes on in Blackjack (e.g. aces can be 1 or 11, kings can be 10)
        :param suit: one of 'diamond', 'spade', 'club', 'heart', or None if the card is generic across all suits
        """
        self.name = name
        self.values = values
        self.suit = suit

    def __str__(self):
        """
        :return: string representation of card in the format "NAME of SUIT"
        """
        return '{0} of {1}'.format(self.get_name(), self.get_suit())

    def get_values(self):
        """
        :return: the list of values that this card has
        """
        return self.values

    def get_name(self):
        """
        :return: the title of this card
        """
        return self.name

    def get_suit(self):
        """
        :return: the suit of this card (None if generic)
        """
        return self.suit

    def set_suit(self, suit: str):
        """
        Sets the suit of this card to the given suit

        :param suit: one of 'diamond', 'spade', 'club', 'heart' (raises ValueError if not one of these)
        """
        if suit not in ['diamond', 'spade', 'club', 'heart']:
            raise ValueError('invalid suit')
        self.suit = suit
