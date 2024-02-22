import unittest
from Labs.src.lab1_3_2 import find_unsorted_part


class TestUnsortedPart(unittest.TestCase):
    def testgivenarray(self):
        result = find_unsorted_part([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
        self.assertEqual(result, (3, 9))

    def testsorted_array(self):
        result = find_unsorted_part([1, 2, 3, 4, 5])
        self.assertEqual(result, (-1, -1))

    def test_sorted_reversed_array(self):
        result = find_unsorted_part([5, 4, 3, 2, 1])
        self.assertEqual(result, (0, 4))

    def test_single_element_array(self):
        result = find_unsorted_part([2])
        self.assertEqual(result, (-1, -1))


if __name__ == "__main__":
    unittest.main()
