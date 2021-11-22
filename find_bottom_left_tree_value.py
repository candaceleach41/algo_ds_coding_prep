"""
Given the root of a binary tree, return the leftmost value in the last row of the
tree.

Example 1:
            2               <------------- Level 0
          /   \
         1     3            <------------- Level 1

Input: root = [2,1,3]
Output: 1

Example 2:
            1               <------------- Level 0
          /   \
         2     3            <------------- Level 1
        /    /   \
       4    5     6         <------------- Level 2
           /
          7                 <------------- Level 3

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""


# Time: O(n)
# Space: O(n)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_bottom_left_value(root):
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


#  another solution going right to left level order
from collections import deque


def find_bottom_left_value2(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    return node.val


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)

    print(find_bottom_left_value(root))
