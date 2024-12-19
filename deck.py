from card import Card

class Deck:

    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        """Create a full deck of all 52 cards."""
        deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                deck.append(Card(suit, rank))
        return deck
    