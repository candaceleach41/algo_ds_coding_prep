"""
Given the root of a binary tree, return the zigzag level order traversal of its
nodes' values. (i.e., from left to right, then right to left for the next level
and alternate between).

Example 1:
                3
              /   \
             9     20
                  /   \
                 15    7


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
"""
import collections


# Time: O(n)
# Space: O(n)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    deque = collections.deque()
    if root:
        deque.append(root)

    result = []
    level = 0
    while deque:
        lev = []
        for _ in range(len(deque)):
            node = deque.popleft()
            lev.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        if level % 2 == 1:
            lev.reverse()
        result.append(lev)
        level += 1
    return result
