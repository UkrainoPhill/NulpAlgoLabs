import unittest
from NulpAlgoLabs.src.note_on_board import put_on_board


class TestPutOnBoard(unittest.TestCase):
    def test_given_numbers(self):
        result = put_on_board(10, 2, 3)
        self.assertEqual(result, 9)

    def test_big_numbers(self):
        result = put_on_board(2, 1000000000, 999999999)
        self.assertEqual(result, 1999999998)

    def test_small_numbers(self):
        result = put_on_board(4, 1, 1)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
