class Node:
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.value = value
        self.priority = priority


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_root_none_insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self.insert(self.root, value, priority)

    def insert(self, node, value, priority):
        if priority >= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self.insert(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self.insert(node.right, value, priority)

    def is_root_none_pop(self):
        if self.root is None:
            return None
        else:
            return self.pop(self.root)

    def pop(self, node):
        if node.left is not None:
            value, priority = self.pop(node.left)
            if node.left.priority == priority:
                node.left = None
            return value, priority
        else:
            return node.value, node.priority

    def print_inorder(self, node):
        if not node:
            return
        self.print_inorder(node.left)
        print(node.value, node.priority)
        self.print_inorder(node.right)

