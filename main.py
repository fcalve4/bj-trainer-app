import random
from shoe import Shoe

class BlackjackTrainer:
    def __init__(self):
        pass
    
    def deal_card(self, shoe):
        return shoe.pop()
    
    def calculate_hand_value(self):
        pass

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

    
    