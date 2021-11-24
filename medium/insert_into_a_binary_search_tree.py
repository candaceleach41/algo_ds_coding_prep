"""
You are given the root node of a binary search tree (BST) and a value to insert
into the tree. Return the root node of the BST after the insertion. It is guaranteed
that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the
tree remains a BST after insertion. You can return any of them.

Example 1:

                    4                                       4
                 /    \                                   /   \
                2      7                                 2     7
              /   \                                    /  \   /
             1     3                                  1   3  5

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_int_bst(root, val):
    node = root
    while node:
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right
        else:
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left
    return TreeNode(val)
