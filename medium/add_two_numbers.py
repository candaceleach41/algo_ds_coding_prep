"""
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Example 1:

                2 -> 4 -> 3
                5 -> 6 -> 4
              --------------
                7 -> 0 -> 8


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(list1, list2):
    cur = dummy = Node(-1)
    carry = 0

    while list1 or list2 or carry:
        if list1:
            carry += list1.val
            list1 = list1.next
        if list2:
            carry += list2.val
            list2 = list2.next
        cur.next = Node(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.nexy
