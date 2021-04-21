"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

    1 -> 2 -> 3 -> 4 -> 5
    1 -> 4 -> 3 -> 2 -> 5

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

    7 -> 9 -> 6 -> 6 -> 7 -> 8 -> 3 -> 0 -> 9 -> 5

    7 -> 9 -> 6 -> 6 -> 8 -> 7 -> 3 -> 0 -> 9 -> 5

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:

Input: head = [1], k = 1
Output: [1]
"""


# Time: O(n) - n is the length of the nodes
# Space: O(1) - not using extra storage and swapping is done in-place
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def swap_nodes(head, k):
    slow = head
    fast = head

    for _ in range(k - 1):
        fast = fast.next
    k_node = fast

    while fast.next:
        slow = slow.next
        fast = fast.next

    k_node.val, slow.val = slow.val, k_node.val
    return head
