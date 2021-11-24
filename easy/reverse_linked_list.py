"""
Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:
1 -> 2 -> 3 -> 4 -> 5

5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Time: O(n) - n is the length of nodes
# Space: O(1) - reversing in-place
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = None

    if not head or head.next:
        return head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
