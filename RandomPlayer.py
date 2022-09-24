import random
from Player import Player
# player that play randomly


class RandomPlayer(Player):  # inheritance from player
    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        random.shuffle(self.hand.array)
        for i in self.hand.array:  # playing randomly by choosing randomly domino from his hand and try to play with it
            if board.add(i):
                self.hand.remove_domino(i)
                return True
            elif board.add(i, False):  # first try to the right and  than to the left
                self.hand.remove_domino(i)
                return True
        return False

    def __init__(self, name, age, hand):  # define al the fields by player
        super().__init__(name, age, hand)
