class Card():

    SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    RANKS = [
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),
        ('Jack', 10),
        ('Queen', 10),
        ('King', 10),
        ('Ace', 11)
    ]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    