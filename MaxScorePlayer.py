from Player import Player
import copy
# a player that maximize is chances to win by playing with the domino that have the highest value


class MaxScorePlayer(Player):  # inheritance from player

    def __init__(self, name, age, hand):   # define all the fields by using player
        super().__init__(name, age, hand)

    def play(self, board):  # play by try to use his domino that have the highest value
        arranged_hand = copy.deepcopy(self.hand.array)
        sorted(arranged_hand, reverse=True)
        for i in sorted(arranged_hand, reverse=True):
            if board.add(i):
                self.hand.remove_domino(i)
                return True
            elif board.add(i, False):  # first try to the right and  than to the left
                self.hand.remove_domino(i)
                return True
        return False

    def __str__(self):  # print his name age hand and current score and say i can win the game as excepted
        return f'Name:{self.name}, Age:{self.age}, Hand:{self.hand}, Score:{self.score()}, I can win the game!'

    def __repr__(self):
        return self.__str__()

