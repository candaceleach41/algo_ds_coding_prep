"""
Given the root of a binary tree, return the vertical order traversal
of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from
left to right.


Example 1:
                    3
                  /   \
                9      20
                     /    \
                    15     7

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
                    3
                  /   \
                9      8
              /  \    /  \
             4   0   1    7

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
                    3
                  /   \
                9      8
              /  \    /  \
             4   0   1    7
               /      \
              5        2

Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

Example 4:
Input: root = []
Output: []
"""


# Time: O(n log n) - because the keys are sorted
# Space: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_order(root):
    if root is None:
        return []

    queue = list()
    queue.append([root, 0])
    dist_map = {}

    while len(queue) > 0:
        node, level = queue.pop(0)
        if not level in dist_map:
            dist_map[level] = [node.val]
        else:
            dist_map[level].append(node.val)
            if node.left is not None:
                queue.append(node.left, level - 1)
            if node.right is not None:
                queue.append(node.right, level + 1)

        sorted_keys = sorted(dist_map.keys())
        vert_order = []

        for i in sorted_keys:
            vert_order.append(dist_map[i])
        return vert_order
