from unittest import TestCase
from Domino import Domino
from Team import Team
from Board import Board
from Hand import Hand
from NaivePlayer import NaivePlayer


class Testteam(TestCase):

    def setUp(self):
        self.d1 = Domino(1, 2)
        self.d2 = Domino(3, 6)
        self.d3 = Domino(2, 5)
        self.hand1 = Hand([self.d1, self.d2, self.d3])
        self.hand2 = Hand([self.d1, self.d2])
        self.hand3 = Hand([])
        self.player1 = NaivePlayer('kobi', 24, self.hand1)
        self.player2 = NaivePlayer('omer', 28, self.hand2)
        self.player3 = NaivePlayer('noa', 15, self.hand3)
        self.team1 = Team('older', [self.player2, self.player1])
        self.team2 = Team('younger', [self.player3, self.player1])
        self.team3 = Team('noaT', [self.player3])

    def test_get_team(self):
        self.assertFalse(self.team1.get_team() == [self.player2, self.player1])

    def test_score_team(self):
        self.assertEqual(self.team1.score_team(), 31)

    def test_has_dominoes_team(self):
        self.assertTrue(self.team1.has_dominoes_team())
        self.assertFalse(self.team3.has_dominoes_team())

    def test_play(self):
        board1 = Board(28)
        self.assertFalse(self.team3.play(board1))
        self.assertTrue(self.team1.play(board1))
        self.assertEqual(board1.array, [self.d1])

    def test_str(self):
        self.assertEqual(self.team1.__repr__(), f'Name {self.team1.name}, Score team: {self.team1.score_team()}, Players: Name: {self.player2.name}, Age: {self.player2.age}, Hand: {self.player2.hand}, Score: {self.player2.score()} Name: {self.player1.name}, Age: {self.player1.age}, Hand: {self.player1.hand}, Score: {self.player1.score()}')
