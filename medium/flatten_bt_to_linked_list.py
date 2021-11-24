"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:

                        1               1
                     /    \              \
                    2      5              2
                  /   \     \              \
                 3     4     6              3
                                             \
                                              4
                                               \
                                                5
                                                 \
                                                  6

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def dfs(root):
        if not root:
            return None

        left_tail = dfs(root.left)
        right_tail = dfs(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        last = right_tail or left_tail or root
        return last

    dfs(root)
