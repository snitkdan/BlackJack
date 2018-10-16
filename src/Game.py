from Hand import Hand
from Deck import Deck
from MaxHeap import MaxHeap

class Game(object):
    """
    This class manages the state of a standard game of BlackJack with N human players
    """
    def __init__(self, player_names: [str], pre_deal=False):
        """
        Constructs a new game of BlackJack in which the first player in the
        list of players has the first turn

        :param player_names: the list of players who will be playing (raises ValueError if player_names is empty
        """
        if len(player_names) < 1:
            raise ValueError('Cannot create a game with no players')
        if len(player_names) > 26:
            raise ValueError('Cannot have more than 26 players for BlackJack')
        self.hands = [Hand(name) for name in player_names]
        self.current_player = 0
        self.deck = Deck()
        if pre_deal:
            for hand in self.hands:
                hand.add_card(self.deck.draw())
                hand.add_card(self.deck.draw())

    def is_game_over(self):
        """
        :return: True if the last player has finished their turn, and False otherwise
        """
        return self.current_player >= len(self.hands)

    def __finishturn(self):
        """
        Updates the rankings of who is in the lead, and moves to the next player (or does nothing if the game is already over)
        """
        if not self.is_game_over():
            self.current_player += 1

    def get_current_hand(self):
        """
        :return: the hand of the current player (raises ValueError if the game is over)
        """
        if self.is_game_over():
            raise ValueError('Cannot get the current hand if the game is over')
        return self.hands[self.current_player]

    def get_current_player_name(self):
        return self.get_current_hand().get_name()

    def hit(self, card=None):
        """
        :param: card to use as next draw (will be drawn from the deck if not provided)
        :return: False if the hit resulted in a bust, and True otherwise. (raises ValueError if the game is already over
        or the deck is out of cards)
        """
        if self.is_game_over():
            raise ValueError('Cannot hit when game is over!')
        card = card if card else self.deck.draw()
        if not card:
            raise ValueError('Ran out of cards')
        current_hand = self.hands[self.current_player]
        current_hand.add_card(card)
        if current_hand.is_bust():
            self.__finishturn()
            return False
        return True

    def stay(self):
        """
        Transitions to the next player, updating the necessary rankings (raises ValueError if the game is already over)
        """
        if self.is_game_over():
            raise ValueError('Cannot stay when game is over!')
        self.__finishturn()

    def get_rankings(self):
        """
        :return: the names of the players in the order of ranking (i.e. 1st place, 2nd place, etc.) (raises ValueError
        if the game is not over yet)
        """
        if not self.is_game_over():
            raise ValueError('Game is still in progress!')
        h = MaxHeap(len(self.hands), self.hands)
        ordered_hands = [h.removeMax() for _ in range(len(self.hands))]
        return [hand.get_name() for hand in ordered_hands]

    def get_winner(self):
        """
        :return: the name of the first place winner of the game (raises ValueError if the game is not over yet)
        """
        return self.get_rankings()[0]



