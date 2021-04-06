"""
Given the root of a binary tree, return the leftmost value
in the last row of the tree.

Example 1:
                2
              /   \
            1      3

Input: root = [2,1,3]
Output: 1

Example 2:
                2
              /   \
            1      3
           /     /   \
          4     5     6
               /
              7

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""

# This problem can be solved using BFS or DFS

class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS
def find_bottom_left_value_bfs(self, root):
    levels = [root]
    ans = 0
    while levels:
        nxt = []
        for node in levels:
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        if not nxt:
            ans = levels[0].val
            break
        levels = nxt
    return ans
