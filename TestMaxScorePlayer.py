from unittest import TestCase
from Domino import Domino
from Hand import Hand
from Board import Board
from MaxScorePlayer import MaxScorePlayer


class TestMaxScorePlayer(TestCase):

    def test_play(self):

        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(3, 5)
        hand1 = Hand([d1, d2, d3])
        b1 = Board(20, [])
        n_player = MaxScorePlayer('kobi', 24, hand1)
        self.assertTrue(n_player.play(b1))
        self.assertEqual(n_player.hand.array, [d1, d3])
        self.assertTrue(n_player.play(b1))
        self.assertFalse(n_player.play(b1))

    def test_str(self):
        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(3, 5)
        hand1 = Hand([d1, d2, d3])
        n_player = MaxScorePlayer('kobi', 24, hand1)
        self.assertEqual(n_player.__repr__(), f'Name:{n_player.name}, Age:{n_player.age}, Hand:{n_player.hand}, Score:{n_player.score()}, I can win the game!')



