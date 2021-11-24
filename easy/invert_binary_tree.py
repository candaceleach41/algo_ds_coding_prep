"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

                4                                   4
             /     \                             /     \
            2       7                           7       2
          /   \   /   \                       /   \   /   \
        1      3 6     9                    9      6 3     1

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return root

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
