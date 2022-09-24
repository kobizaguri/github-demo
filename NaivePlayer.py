from Player import Player
# player that play automatically without thinking about the game.


class NaivePlayer(Player):  # inheritance from player

    def __init__(self, name, age, hand):  # define al the fields by player
        super().__init__(name, age, hand)

    def play(self, board):  # play by trying to use the first domino in his hand and so on until he can use the domino
        for i in self.hand.array:
            if board.add(i):
                self.hand.remove_domino(i)
                return True
            elif board.add(i, False):  # first try to the right and  than to the left
                self.hand.remove_domino(i)
                return True
        return False

