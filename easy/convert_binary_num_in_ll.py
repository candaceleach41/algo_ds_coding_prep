"""
Given head which is a reference node to a singly-linked list. The value of each node
in the linked list is either 0 or 1. The linked list holds the binary
representation of a number.

Return the decimal value of the number in the linked list.

Example 1:

1 -> 0 -> 1

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Space: O(1)
def convert_bin_num(head):
    num = head.next
    while head.next:
        num = num * 2 + head.next.val
        head = head.next
    return num


# Time: O(n)
# Space: O(1)
def convert_bin_num_bit_manp(head):
    num = head.next
    while head.next:
        num = (num << 1) | head.next.val
        head = head.next
    return num

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(0)
    head.next.next = Node(1)

    convert_bin_num(head)
    convert_bin_num_bit_manp(head)
