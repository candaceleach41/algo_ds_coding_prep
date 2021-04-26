"""
Given the root of a binary tree, return the bottom-up level order traversal of its
nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:

            3
          /   \
         9    20
             /  \
            15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n)
# Space: O(n)
def level_order(root):
    if root is None:
        return []

    queue = []
    result = []
    queue.append(root)

    while queue:
        ans = []
        for i in range(len(queue)):
            node = queue.pop(0)
            ans.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        result.append(ans)
    return result[::-1]
