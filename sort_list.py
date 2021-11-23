"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

    4 -> 2 -> 1 -> 3
           |
           v
    1 -> 2 -> 3 -> 4


Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

    -1 -> 5 -> 3 -> 4 -> 0
                |
                v
    -1 -> 0 -> 3 -> 4 -> 5

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105


Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e.
constant space)?
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_list(head):
    def merge_sort(head):
        if not head or not head.next:
            return head

        left = slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)
        return merge(left_sorted, right_sorted)

    def merge(list_1, list_2):
        dummy = Node(-1)
        prev = dummy

        while list_1 and list_2:
            if list_1.val <= list_2.val:
                prev.next = list_1
                list_1 = list_1.next
            else:
                prev.next = list_2
                list_2 = list_2.next
        prev.next = list_1 or list_2
        return dummy.next

    return merge_sort(head)
