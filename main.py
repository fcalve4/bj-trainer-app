import random

class BlackjackTrainer:
    def __init__(self):
        self.shoe = self.create_shoe(num_decks=2)
        
    
    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = []
        for suit in suits:
            for rank in ranks:
                card = {'suit': suit, 'rank': rank}
                deck.append(card)
        return deck
    
    def create_shoe(self, num_decks):
        shoe = []
        for _ in range(num_decks):
            shoe.extend(self.create_deck())
        random.shuffle(shoe)
        return shoe
    
    




if __name__ == '__main__':
    game = BlackjackTrainer()
    for i in range(len(game.shoe)):
        print(i + 1, game.shoe[i])
    