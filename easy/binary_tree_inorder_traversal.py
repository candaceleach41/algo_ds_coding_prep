"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

            1
             \
              2
            /
           3


Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:

            1
          /
         2

Input: root = [1,2]
Output: [2,1]

Example 5:

            1
             \
              2

Input: root = [1,null,2]
Output: [1,2]
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    result = []

    def traversal(node):
        if node:
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)

    traversal(root)
    return result


# one line solution
def inorder_traversal_2(root):
    return inorder_traversal_2(root.left) + [root.val] + inorder_traversal_2(root.right) if root else []
