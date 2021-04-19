"""
Given the head of a linked list and an integer val, remove all the nodes of
the linked list that has Node.val == val, and return the new head.


Example 1:

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
               |
               v
        1 -> 2 -> 3 -> 4 -> 5

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
"""

# Time: O(n) - n is the length of the nodes
# Space: O(1) - not using extra space
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def remove_elements(self, head, val):
        if not head:
            return head

        while head and head.val == val:
            head = head.next

        cur_node = head
        while cur_node and cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return head
