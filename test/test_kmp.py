import unittest
from src.kmp import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = kmp_search("ABBBACBACCCAABB", "BAC")
        self.assertEqual(result, [3, 6])

    def test_null(self):
        result = kmp_search("", "")
        self.assertEqual(result, [])

    def test_similar(self):
        result = kmp_search("AAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAA")
        self.assertEqual(result, [0])

    def test_bigger_pattern(self):
        result = kmp_search("A", "AAAAAA")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
