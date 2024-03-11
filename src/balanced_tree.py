class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def balanced_tree(root: BinaryTree):
    def dfs(node):
        if not node:
            return [True, 0]
        left = dfs(node.left)
        right = dfs(node.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        if left[1] > right[1]:
            max_height = left[1]
        else:
            max_height = right[1]
        return [balanced, 1 + max_height]
    return dfs(root)[0]
