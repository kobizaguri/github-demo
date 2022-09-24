from abc import ABC, abstractmethod
from Hand import Hand


class Player(ABC):  # abstract class because we cant have a player without a specialization

    def __init__(self, name, age, hand):  # define all the fields in player
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):  # check what is the score of the player by sum all the values of all the dominoes in his hand
        player_score = 0
        if isinstance(self.hand, Hand):
            for i in self.hand.array:
                player_score += i.right
                player_score += i.left
        return player_score

    def has_dominoes(self):  # check if the player have domino left in his hand
        if len(self.hand) > 0:
            return True
        else:
            return False

    @abstractmethod
    def play(self, board):  # abstract method because we dont have a player that is just a player so he cant play
        pass

    def __str__(self):  # print the name, age, hand and score of the player
        return f'Name: {self.name}, Age: {self.age}, Hand: {self.hand}, Score: {self.score()}'

    def __repr__(self):
        return self.__str__()

