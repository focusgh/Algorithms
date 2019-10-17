import unittest

from Python.searches import binary_search_variants


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_left(self):
        res = binary_search_variants.binary_search_left([1, 2, 3, 3, 4, 4, 4, 5], 41)
        self.assertEqual(-1, res)

    def test_binary_search_right(self):
        res = binary_search_variants.binary_search_right([1, 2, 3, 3, 4, 4, 4, 5, 5], 9)
        self.assertEqual(-1, res)

    def test_binary_search_not_less(self):
        res = binary_search_variants.binary_search_left_not_less([1, 2, 2, 3, 3, 4, 4, 4, 5], 5)
        self.assertEqual(8, res)

    def test_binary_search_right_not_greater(self):
        sorted_collection = [1, 2, 2, 4, 4, 4, 5]
        search_item = 3
        res = binary_search_variants.binary_search_right_not_greater(sorted_collection, search_item)
        self.assertEqual(3, res)


if __name__ == '__main__':
    unittest.main()
