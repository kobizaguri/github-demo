from unittest import TestCase
from Domino import Domino


class TestDomino(TestCase):

    def test_exceptions(self):
        try:
            Domino(7, 2)
        except Exception as e:
            self.assertEqual(str(e), "ERROR This variable can get values between 0 to 6")
        try:
            Domino(2, -1)
        except Exception as e:
            self.assertEqual(str(e), "ERROR This variable can get values between 0 to 6")

    def test_get_left(self):
        domino1 = Domino(1, 2)
        self.assertEqual(1, domino1.get_left())

    def test_get_right(self):
        domino1 = Domino(1, 2)
        self.assertEqual(2, domino1.get_right())

    def test_flip(self):
        domino1 = Domino(1, 2)
        domino2 = Domino(2, 1)
        domino3 = Domino(1, 3)
        flipped_dom = domino1.flip()
        self.assertEqual(1, flipped_dom.get_right())
        self.assertEqual(2, flipped_dom.get_left())
        self.assertTrue(domino1 == domino2)
        self.assertTrue(domino1 != domino3)
        self.assertFalse(domino1 == domino3)
        self.assertFalse(domino1 != domino2)
        self.assertTrue(domino3 > domino1)
        self.assertFalse(domino2 > domino1)
        self.assertTrue(1 in domino1)
        self.assertFalse(5 in domino3)

    def test_str(self):
        domino1 = Domino(5, 6)
        self.assertEqual(domino1.__str__(), '[5|6]')
        self.assertEqual(domino1.__repr__(), '[5|6]')






