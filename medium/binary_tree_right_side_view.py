"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:

                    1           <----
                 /     \
                2       3       <----
                 \       \
                  5       4     <----

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    result = []

    def bfs(node, depth, result):
        if not node:
            return

        if depth > len(result) - 1:
            result.append(node.val)
        result[depth] = node.val

        bfs(node.left, depth + 1, result)
        bfs(node.right, depth + 1, result)

    bfs(root, 0, result)
    return result
