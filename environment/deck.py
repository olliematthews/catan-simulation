import numpy.random


class DevelopmentDeck:
    def __init__(self, cards):
        self.cards = []
        for key, value in cards.items():
            self.cards.extend([key] * value)
        
    def random_pick(self):
        return random.choice(self.cards, replace = False)
    

class ResourceDeck:
    def __init__(self, n_cards):
        self.n_cards = n_cards
        self.empty = false
        
    def take(self):
        if self.empty:
            return False
        else:
            self.n_cards -= 1
            self.empty = self.n_cards <= 0
            return True

    def replace(self):
        self.n_cards += 1
