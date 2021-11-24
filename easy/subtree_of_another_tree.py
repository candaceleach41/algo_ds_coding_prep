"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same
structure and node values with a subtree of s. A subtree of s is a tree consists of
a node in s and all of this node's descendants. The tree s could also be considered
as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(s, t):
    def dfs(n, t):
        if not n and not t:
            return True
        if not n or not t:
            return False
        return n.val == t.val and dfs(n.left, t.left) and dfs(n.right, t.right)

    stack = [s]
    while stack:
        n = stack.pop()
        if n.val == t.val and dfs(n, t) and dfs(n, t):
            return True
        if n.left:
            stack.append(n.left)
        if n.right:
            stack.append(n.right)
    return False
