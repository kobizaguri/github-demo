from NaivePlayer import NaivePlayer
from Domino import Domino
from Board import Board
from unittest import TestCase
from Hand import Hand
from Team import Team
from Game import Game


class TestGame(TestCase):
    def setUp(self):
        self.d1 = Domino(1, 2)
        self.d2 = Domino(3, 1)
        self.d3 = Domino(3, 2)
        self.d4 = Domino(4, 6)
        self.d5 = Domino(5, 4)
        self.d6 = Domino(4, 6)
        self.hand1 = Hand([self.d1, self.d2])
        self.hand2 = Hand([self.d3, self.d4])
        self.hand3 = Hand([])
        self.hand4 = Hand([self.d1, self.d2, self.d5])
        self.player1 = NaivePlayer('kobi', 24, self.hand1)
        self.player2 = NaivePlayer('omer', 28, self.hand2)
        self.player3 = NaivePlayer('noa', 15, self.hand3)
        self.player4 = NaivePlayer('ron', 25, self.hand4)
        self.team1 = Team('A', [self.player1])
        self.team2 = Team('B', [self.player2])
        self.team3 = Team('C', [self.player3])
        self.team4 = Team('D', [self.player4])
        self.board1 = Board(28)
        self.board2 = Board(2)
        self.board3 = Board(1)
        self.game1 = Game(self.board1, self.team3, self.team2)
        self.game2 = Game(self.board1, self.team1, self.team3)
        self.game3 = Game(self.board1, self.team4, self.team2)
        self.game4 = Game(self.board1, self.team2, self.team4)
        self.game5 = Game(self.board1, self.team4, self.team4)
        self.game6 = Game(self.board3, self.team2, self.team1)
        self.game7 = Game(self.board3, self.team1, self.team2)
        self.game8 = Game(self.board2, self.team1, self.team1)

    def test_play(self):
        self.assertEqual(self.game6.play(), 'Team A wins Team B')
        self.assertEqual(self.game7.play(), 'Team A wins Team B')
        self.assertEqual(self.game1.play(), 'Team C wins Team B')
        self.assertEqual(self.game2.play(), 'Team C wins Team A')
        self.assertEqual(self.game3.play(), 'Team D wins Team B')
        self.assertEqual(self.game4.play(), 'Team D wins Team B')
        self.assertEqual(self.game5.play(), 'Draw!')













