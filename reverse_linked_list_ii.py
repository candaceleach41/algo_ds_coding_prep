"""
Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.

Example 1:

1 -> 2 -> 3 -> 4 -> 5

1 -> 4 -> 3 -> 2 -> 5

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""


# Time: O(n) - n is the length of the nodes
# Space: O(1) reversing k elements in-place
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# This is using the sliding window approach
def reverse_between(head, left, right):
    dummy = ListNode(-1)
    dummy.next = head

    prev = dummy
    curr = dummy.next

    for i in range(1, left):
        curr = curr.next
        prev = prev.next

    for i in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


# Reverse linked-list logic
def reverse_list(self, head):
    prev, curr, tail = None, head, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev, tail
