"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees
are overlapped while the others are not. You need to merge the two trees into a new
binary tree. The merge rule is that if two nodes overlap, then sum node values up as
the new value of the merged node. Otherwise, the NOT null node will be used as the
node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

                1                   2                           3
             /     \             /     \                      /    \
            3       2           1       3       ----->      4       5
          /                      \       \               /     \      \
         5                        4       7             5       4       7


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(t1, t2):
    if not t1:
        return t2

    if not t2:
        return t1

    stack = [[t1, t2]]
    while stack:
        cur = stack.pop()
        if cur[0] is None or cur[1] is None:
            continue
        cur[0].val += cur[1].val
        if cur[0].left is None:
            cur[0].left = cur[1].left
        else:
            stack.append([cur[0].left, cur[1].left])
        if cur[0].right is None:
            cur[0].right = cur[1].right
        else:
            stack.append([cur[0].right, cur[1].right])
    return t1


# ------------------------ Another Solution Using Recursion -----------------------
def merge_trees_recur(t1, t2):
    if not t2:
        return t1
    if not t1:
        return t2

    t1.val += t2.val

    t1.left = merge_trees_recur(t1.left, t2.left)
    t1.right = merge_trees_recur(t1.right, t2.right)

    return t1
