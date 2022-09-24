from unittest import TestCase
from Collection import Collection


class TestCollection(TestCase):
    def test_get_collection(self):
        collection = Collection([1, 2, 3])
        array2 = collection.get_collection()
        self.assertEqual(collection.array, array2)

    def test_add(self):
        collection = Collection([1, 2, 3])
        try:
            collection.add(4, True)
        except Exception as e:
            self.assertEqual(str(e), "To add use the right method")

    def test__get_item__(self):
        collection = Collection([1, 2, 3])
        self.assertEqual(3, collection[2])
        self.assertIsNone(collection[3])

    def test_eq_ne_len_contain(self):
        collection1 = Collection([1, 2, 3])
        collection2 = Collection([1, 2, 3])
        self.assertTrue(collection1 == collection2)
        self.assertFalse(collection1 != collection2)
        collection1 = Collection([1, 2, 4])
        collection2 = Collection([1, 2, 3])
        self.assertFalse(collection1 == collection2)
        self.assertTrue(collection1 != collection2)
        self.assertEqual(3, len(collection1))
        self.assertTrue(1 in collection1)
        self.assertFalse(4 in collection2)

    def test__str__(self):
        collection1 = Collection([1, 2, 3])
        string = '123'
        self.assertEqual(string, collection1.__str__())
        self.assertEqual(string, collection1.__repr__())





