"""
Given a binary search tree, return a balanced binary search tree with the same
node values.

A binary search tree is balanced if and only if the depth of the two subtrees
of every node never differ by more than 1.

If there is more than one answer, return any of them.



Example 1:

    1                                   2
     \                                /   \
      2                             1      3
       \                                    \
        3                                    4
         \
          4

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balance_bst(root):
    nodes = []

    def inorder(root):
        if root is None:
            return

        inorder(root.left)
        nodes.append(root)
        inorder(root.right)

    inorder(root)

    def bst(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = bst(start, mid - 1)
        root.right = bst(mid + 1, end)
        return root

    return bst(0, len(nodes) - 1)
