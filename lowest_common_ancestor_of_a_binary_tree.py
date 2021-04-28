"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”


Example 1:

                    3
                 /      \
                5        1
              /   \    /   \
             6     2  0     8
                 /   \
                7     4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

                     3
                 /      \
                5        1
              /   \    /   \
             6     2  0     8
                 /   \
                7     4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
according to the LCA definition.
"""

# Time: O(n)
# Space: O(n)
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    left_search_result = lowest_common_ancestor(root.left, p, q)
    right_search_result = lowest_common_ancestor(root.right, p, q)

    return root if left_search_result and right_search_result else left_search_result or right_search_result

