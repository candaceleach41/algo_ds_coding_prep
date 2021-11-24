"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree
rooted with that node. If such a node does not exist, return null.

Example 1:

                4
              /   \
             2     7
           /   \
          1     3

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
"""


# Time: O(log n)
# Space: O(1)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search_bst(root, val):
    while root:
        if root.val == val:
            return root
        elif root.val < val:
            root = root.right
        else:
            root = root.left
    return None
