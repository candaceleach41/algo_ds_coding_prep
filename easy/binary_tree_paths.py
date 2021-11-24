class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    if root is None:
        return []

    result = []
    stack = [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            result.append(ls + str(node.val))
        if node.right:
            stack.append((node.right, ls + str(node.val) + "->"))
        if node.left:
            stack.append((node.left, ls + str(node.val) + "->"))
    return result
