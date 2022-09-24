import copy


class Team:

    def __init__(self, name, players):  # define all the fields in team class
        self.name = name
        self.__players = players

    def get_team(self):  # returning all the players in the team (by doing deep copy)
        return copy.deepcopy(self.__players)

    def score_team(self):  # check the score of all the team by check the score of every player in the team
        summer = 0
        for player in self.__players:
            summer += player.score()
        return summer

    def has_dominoes_team(self):   # check if the team still have dominoes by checking each player in the team
        for player in self.__players:
            if player.has_dominoes():
                return True
        return False

    def play(self, board):  # playing with the first layer in the team that can play
        for player in self.__players:
            if player.play(board):
                return True
        return False

    def __str__(self):  # print the name and the score of the team and all the players in the as they printed in their class
        string_of_all = ''
        for player in self.__players:
            string_of_all += ' ' + player.__str__()
        return f"Name {self.name}, Score team: {self.score_team()}, Players:{string_of_all}"

    def __repr__(self):
        return self.__str__()
