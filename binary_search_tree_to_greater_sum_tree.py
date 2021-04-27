"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that
every key of the original BST is changed to the original key plus sum of all keys
greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as
538: https://leetcode.com/problems/convert-bst-to-greater-tree/

Example 1:

                            4
                         /     \
                        1       6
                     /    \    /   \
                    0      2   5    7
                            \        \
                             3        8

Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
Example 3:

Input: root = [1,0,2]
Output: [3,3,2]
Example 4:

Input: root = [3,2,4,1]
Output: [7,9,4,10]
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) - n is the number of nodes
# Space: O(n) - using stack for extra space
def bst_to_gst(root):
    sum = 0
    cur = root
    stack = []
    while stack or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.right
        cur = stack.pop()
        cur.val += sum
        sum = cur.val
        cur = cur.left
    return root


# another solution
def bst_to_gst_2(self, root):
    val = 0
    def inorder(node):
        if node:
            inorder(node.right)
            node.val += self.val
            self.val = node.val
            inorder(node.left)
    inorder(root)
    return root
