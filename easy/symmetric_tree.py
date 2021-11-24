"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
symmetric around its center).

Example 1:

                1
             /     \
            2       2
          /  \     /  \
         3    4   4    3


Input: root = [1,2,2,3,4,4,3]
Output: true
"""
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    if not root:
        return True

    queue = deque([(root.left, root.right)])
    while queue:
        l, r = queue.popleft()

        if l and r and l.val == r.val:
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        elif l == r:
            continue
        else:
            return False

    return True
