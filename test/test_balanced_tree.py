import unittest
from src.balanced_tree import *


class TestBalancedTree(unittest.TestCase):
    def test_given_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        result = balanced_tree(root)
        self.assertEqual(result, True)

    def test_root_tree(self):
        root = BinaryTree(1)
        result = balanced_tree(root)
        self.assertEqual(result, True)

    def test_empty_tree(self):
        result = balanced_tree(None)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
