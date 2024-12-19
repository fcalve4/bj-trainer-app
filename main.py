import random
from shoe import Shoe

class BlackjackTrainer:
    def __init__(self):
        pass
    
    def deal_card(self, shoe: list):
        return shoe.pop()
    
    def calculate_hand_value(self, hand: list):
        total = 0
        aces = 0

        for card in hand:
            if card == 'A':
                aces += 1
                total += 11
            else:
                total += card

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total, 'soft' if aces else 'hard'

    def play_hand(self):
        pass

    def check_strategy_sheet(self):
        pass

    def play_shoe(self):
        pass
    




if __name__ == '__main__':
    game = BlackjackTrainer()
    
    shoe = Shoe(6)

    for i in range(len(shoe.cards)):
        print(shoe.cards[i])

    
    