import random
from deck import Deck

class Shoe():
    def __init__(self, num_decks):
        self.cards = self.create_shoe(num_decks=num_decks)

    def create_shoe(self, num_decks):
        deck = Deck()
        shoe = []

        for _ in range(num_decks):
            shoe.extend(deck.create_deck())
        
        random.shuffle(shoe)
        return shoe
