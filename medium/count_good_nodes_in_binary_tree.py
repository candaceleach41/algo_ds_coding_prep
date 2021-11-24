"""
Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root):
    if root.left is None and root.right is None:
        return 1
    else:
        ans = 0
        stack = [[root, root.val]]

        # Standard DFS
        while stack:
            curr, curr_max = stack.pop()

            if curr.val >= curr_max:
                ans += 1
                curr_max = curr.val

            if curr.right is not None:
                stack.append([curr.right, curr_max])
            if curr.left is not None:
                stack.append([curr.left, curr_max])
        return ans
