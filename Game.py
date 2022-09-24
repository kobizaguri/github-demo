class Game:

    def __init__(self, board, team1, team2):  # define all the fields in Game
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        while self.board.max_capacity != len(self.board):  # both team play until one of the below happen:
            bool_team1 = self.team1.play(self.board)
            if self.board.max_capacity == len(self.board):  # board is full
                break
            if not self.team1.has_dominoes_team():  # team1 are out of dominoes
                return f'Team {self.team1.name} wins Team {self.team2.name}'

            bool_team2 = self.team2.play(self.board)

            if not self.team2.has_dominoes_team():  # team2 are out of dominoes
                return f'Team {self.team2.name} wins Team {self.team1.name}'

            if not bool_team1 and not bool_team2:  # both teams cant put dominoes on the board any more
                if self.team1.score_team() > self.team2.score_team():   # the team with more points loss
                    return f'Team {self.team2.name} wins Team {self.team1.name}'

                elif self.team2.score_team() > self.team1.score_team():
                    return f'Team {self.team1.name} wins Team {self.team2.name}'
                else:
                    return 'Draw!'  # if both teams have the same amount of points it's a draw

        if self.team1.score_team() > self.team2.score_team():
            return f'Team {self.team2.name} wins Team {self.team1.name}'
        elif self.team2.score_team() > self.team1.score_team():
            return f'Team {self.team1.name} wins Team {self.team2.name}'
        else:
            return 'Draw!'
        # when the game is over the team that won are announced as the winner
