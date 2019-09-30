import unittest

from Python.searches import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        res = binary_search.binary_search([1, 2, 3, 4], 3)
        print(res)
        self.assertEqual(2, res)

    def test_binary_search_by_recursion(self):
        res = binary_search.binary_search_by_recursion([1, 2, 3, 4, 5], 0)
        print(res)
        self.assertEqual(-1, res)

    def test_binary_search_by_bisect(self):
        res = binary_search.binary_search_by_bisect([1, 2, 3, 4, 5], 3)
        print(res)
        self.assertEqual(2, res)


if __name__ == '__main__':
    unittest.main()
