from unittest import TestCase
from Player import Player
from Hand import Hand
from Domino import Domino
from NaivePlayer import NaivePlayer


class TestPlayer(TestCase):

    def setUp(self):
        self.d1 = Domino(1, 2)
        self.d2 = Domino(3, 6)
        self.d3 = Domino(2, 5)
        self.hand1 = Hand([self.d1, self.d2, self.d3])
        self.n_player = NaivePlayer('kobi', 24, self.hand1)

    def test_score(self):
        self.assertEqual(self.n_player.score(), 19)

    def test_has_dominoes(self):
        self.assertTrue(self.n_player.has_dominoes())
        hand2 = Hand([])
        player2 = NaivePlayer('omer', 28, hand2)
        self.assertFalse(player2.has_dominoes())

    def test_str(self):
        self.assertEqual(self.n_player.__repr__(), f'Name: {self.n_player.name}, Age: {self.n_player.age}, Hand: {self.n_player.hand}, Score: {self.n_player.score()}')
