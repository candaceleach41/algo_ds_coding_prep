"""
Given the root of a binary search tree and a target value, return the value in the
BST that is closest to the target.



Example 1:

                    4
                  /   \
                 2     5
               /   \
              1     3

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""


# Time: O(log n)
# Space: O(1) 
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(self, root, target):
    self.closest = float("inf")

    def dfs(root, value):
        if not root:
            return

        if abs(root.val - target) < abs(self.closest - target):
            self.closest = root.val

        if target < root.val:
            dfs(root.left, target)

        if target > root.val:
            dfs(root.right, target)

    dfs(root, target)
    return self.closest
