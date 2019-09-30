import unittest

from Python.searches import binary_search_variants


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_left(self):
        res = binary_search_variants.binary_search_left([1, 2, 3, 3, 4, 4, 4, 5], 41)
        print(res)
        self.assertEqual(-1, res)

    def test_binary_search_right(self):
        res = binary_search_variants.binary_search_right([1, 2, 3, 3, 4, 4, 4, 5, 5], 9)
        print(res)
        self.assertEqual(-1, res)


if __name__ == '__main__':
    unittest.main()
