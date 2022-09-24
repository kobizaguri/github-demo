from RandomPlayer import RandomPlayer
from Domino import Domino
from Board import Board
from unittest import TestCase
from Hand import Hand


class TestRandomPlayer(TestCase):

    def test_play(self):

        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(2, 5)
        d4 = Domino(1, 4)
        hand1 = Hand([d1, d2, d3, d4])
        b1 = Board(20, [])
        n_player = RandomPlayer('kobi', 24, hand1)
        self.assertTrue(n_player.play(b1))
        self.assertTrue(n_player.play(b1))
        self.assertTrue(n_player.play(b1))
        self.assertFalse(n_player.play(b1))

    def test_str(self):
        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(2, 5)
        hand1 = Hand([d1, d2, d3])
        n_player = RandomPlayer('kobi', 24, hand1)
        self.assertEqual(n_player.__str__(), f'Name: kobi, Age: 24, Hand: {n_player.hand}, Score: {n_player.score()}')

