import unittest
from src.binary_tree_priority_queue import *


class TestFindLongestPick(unittest.TestCase):
    def test_delete_max_priority_function(self):
        tree = BinaryTree()
        tree.is_root_none_insert(1.5, 0.1)
        tree.is_root_none_insert(2, 1)
        tree.is_root_none_insert(3, 1)
        tree.is_root_none_insert(2, 2.5)
        tree.is_root_none_insert(3, 3)
        tree.is_root_none_insert(4.3, 4)

        self.assertEqual(tree.is_root_none_pop(), (4.3, 4))

    def test_equal_priority_input_data(self):
        tree = BinaryTree()
        tree.is_root_none_insert(1, 1)
        tree.is_root_none_insert(2, 1)
        tree.is_root_none_insert(3, 1)
        tree.is_root_none_insert(4, 1)
        tree.is_root_none_insert(5, 1)

        self.assertEqual(tree.root.left.value, 2)

    def test_increasing_priority_input_data(self):
        tree = BinaryTree()
        tree.is_root_none_insert(1, 1)
        tree.is_root_none_insert(11, 2)
        tree.is_root_none_insert(111, 3)
        tree.is_root_none_insert(1111, 4)
        tree.is_root_none_insert(11111, 5)

        self.assertEqual(tree.root.left.value, 11)

    def test_empty_tree(self):
        tree = BinaryTree()
        self.assertEqual(tree.is_root_none_pop(), None)


if __name__ == "__main__":
    unittest.main()
