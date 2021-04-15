"""
Given the head of a singly linked list, return true if it is a palindrome.


Example 1:
1 -> 2 -> 2 -> 1
Input: head = [1,2,2,1]
Output: true

Example 2:
1 -> 2
Input: head = [1,2]
Output: false
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev


if __name__ == "__main__":
    # returns True
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next = ListNode(1)
    print((is_palindrome(head)))
