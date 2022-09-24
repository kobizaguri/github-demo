from unittest import TestCase
from Board import Board
from Domino import Domino


class TestBoard(TestCase):

    def test_exceptions(self):
        try:
            Board(29)
        except Exception as e:
            self.assertEqual(str(e), "ERROR This variable can get values between 1 to 28")
        try:
            board1 = Board(5)
            board1.in_left()
        except Exception as e:
            self.assertEqual(str(e), "ERROR The board is empty")
        try:
            board1 = Board(7)
            board1.in_right()
        except Exception as e:
            self.assertEqual(str(e), "ERROR The board is empty")
        try:
            domino1 = Domino(2, 4)
            board1 = Board(1, [domino1.flip()])
            board1.add(domino1)
        except Exception as e:
            self.assertEqual(str(e), "ERROR The board is full")

    def test_in_left(self):
        domino1 = Domino(1, 2)
        board1 = Board(10, [domino1])
        self.assertEqual(1, board1.in_left())

    def test_in_right(self):
        domino1 = Domino(1, 2)
        board1 = Board(10, [domino1])
        self.assertEqual(2, board1.in_right())

    def test_add(self):
        domino1 = Domino(1, 3)
        domino2 = Domino(3, 1)
        domino3 = Domino(3, 1)
        domino4 = Domino(6, 5)
        board1 = Board(5, [domino1])
        board2 = Board(7, [domino1])
        board3 = Board(8, [domino2])
        board4 = Board(18, [domino2])
        board5 = Board(7, [])
        self.assertTrue(board5.add(domino1, False))
        self.assertTrue(board5.add(domino1))
        self.assertTrue(board1.add(domino2))
        self.assertEqual([domino1, domino2], board1.array)
        self.assertTrue(board2.add(domino2, False))
        self.assertEqual([domino2, domino1], board2.array)
        self.assertTrue(board3.add(domino3))
        self.assertEqual([domino2, domino3.flip()], board3.array)
        self.assertTrue(board4.add(domino3, False))
        self.assertEqual([domino3.flip(), domino2], board4.array)
        self.assertFalse(board3.add(domino4))
        self.assertFalse((board3.add(domino4, False)))


    def test_get_item(self):

        domino1 = Domino(3, 1)
        board1 = Board(27, [domino1])
        self.assertEqual(domino1, board1.get_item(0))
        self.assertIsNone(board1.get_item(1))
        self.assertIsNone(board1.get_item(-2))

    def test_eq_ne_contains(self):
        domino1 = Domino(1, 3)
        domino2 = Domino(5, 4)
        domino3 = Domino(4, 2)
        domino4 = Domino(3, 6)
        board1 = Board(7, [domino1, domino4])
        board2 = Board(7, [domino2, domino3])
        board3 = Board(8, [domino1, domino4])
        board4 = Board(7, [domino2, domino3])
        self.assertTrue(domino1 in board1)
        self.assertFalse((domino2 in board1))
        self.assertFalse(board1 == board2)
        self.assertTrue(board1 != board3)
        self.assertFalse(board2 != board4)

    def test_str(self):
        domino1 = Domino(4, 2)
        domino2 = Domino(2, 6)
        board1 = Board(10, [domino1, domino2])
        self.assertEqual('[4|2][2|6]', str(board1))
        self.assertEqual('[4|2][2|6]', board1.__repr__())

