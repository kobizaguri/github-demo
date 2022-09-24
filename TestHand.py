from Domino import Domino
from Hand import Hand
from unittest import TestCase


class TestHand(TestCase):

    def test_add(self):
        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(2, 5)
        hand = Hand([d1])
        hand.add(d2)
        self.assertEqual(hand.array, [d1, d2])
        hand.add(d3, 1)
        self.assertEqual([d1, d3, d2], hand.array)

    def test_remove_domino(self):
        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(2, 5)
        hand = Hand([d1, d2])
        try:
            hand.remove_domino(d3)
        except Exception as e:
            self.assertEqual(str(e), 'ERROR This domino is not in your hand')
        self.assertTrue(hand.remove_domino(d2), 1)
        self.assertEqual(hand.array, [d1])

    def test_eq_ne_gt_con(self):
        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        d3 = Domino(2, 1)
        hand1 = Hand([d1, d2])
        hand2 = Hand([d3, d2])
        self.assertTrue(hand1 == hand2)
        self.assertFalse(hand1 != hand2)
        hand2.add(d3)
        self.assertFalse(hand1 == hand2)
        self.assertFalse(hand1 == [1, 2, 3])
        self.assertTrue(hand1 != hand2)
        self.assertTrue(hand1[0] == d1)
        self.assertEqual(len(hand1), 2)
        hand2.remove_domino(d2)
        self.assertFalse(hand1 == hand2)

    def test_str(self):
        d1 = Domino(1, 2)
        d2 = Domino(3, 6)
        hand1 = Hand([])
        self.assertEqual(str(hand1), '[]')
        hand2 = Hand([d1, d2])
        self.assertEqual((str(hand2)), '[1|2][3|6]')




