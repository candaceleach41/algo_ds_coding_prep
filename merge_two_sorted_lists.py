"""
Merge two sorted linked lists and return it as a sorted list. The
list should be made by splicing together the nodes of the first two lists.


Example 1:

            1 -> 2 -> 4
            1 -> 3 -> 4
        1 -> 1 -> 2 -> 3 -> 4 -> 4

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Recursion
def merge_two_sorted(self, l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1

        l1.next = merge_two_sorted(l1.next, l2)
    return l1 or l2


# Iterative
def merge_two_sorted_iter(l1, l2):
    head = Node()
    curr = head
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return head.next
