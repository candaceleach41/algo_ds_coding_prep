"""
You are given two non-empty linked lists representing two non-negative integers. The
most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Example 1:

        7 -> 2 -> 4 -> 3
             5 -> 6 -> 4
       ------------------
        7 -> 8 -> 0 -> 7

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:

        2 -> 4 -> 3
        5 -> 6 -> 4
      --------------
        8 -> 0 -> 7

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    l1_stack = []
    l2_stack = []

    while l1:
        l1_stack.append(l1.val)
        l1 = l1.next

    while l2:
        l2_stack.append(l2.val)
        l2 = l2.next

    carry = 0
    result = None

    while l1_stack or l2_stack:
        total_sum = carry

        if l1_stack:
            total_sum += l1_stack.pop()

        if l2_stack:
            total_sum += l2_stack.pop()

        carry = total_sum // 10
        total_sum %= 10

        result = Node(total_sum, result)

    if carry != 0:
        result = Node(1, result)

    return result
