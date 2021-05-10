"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

1 -> 2- -> 3 -> 4 -> 5
rotate 1:
    5 -> 1 -> 2- -> 3 -> 4

rotate 2:
    4 -> 5 -> 1 -> 2- -> 3

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""


# This is done using circular linked list
def rotate_right(head, k):
    if not head:
        return None

    if not head.next:
        return head

    last_elem = head
    length = 1

    while last_elem.next:
        last_elem = last_elem.next
        length += 1

    k %= length

    last_elem.next = head
    temp_node = head

    for _ in range(length - k - 1):
        temp_node = temp_node.next

    ans = temp_node.next
    temp_node.next = None

    return ans
