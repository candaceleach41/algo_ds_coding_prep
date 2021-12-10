"""
You are given a doubly linked list which in addition to the next and previous
pointers, it could have a child pointer, which may or may not point to a separate
doubly linked list. These child lists may have one or more children of their own,
and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.


Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:

    1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 -- null
                |
                v
                7 <-> 8 <-> 9 <-> 10 -- null
                      |
                      v
                      11 <-> 12 -- null
"""

# Time: O(n) - n is the length of the list
# Space: O(n) - using stack for additional space
class Node:
    def __init__(self, value, child, next=None, prev=None):
        self.value = value
        self.child = child
        self.next = next
        self.prev = prev


def flatten(head):
    cur = head
    stack = []
    while head:
        if head.child:
            if head.next:
                stack.append(head.next)
            head.next = head.child
            head.next.prev = head
            head.child = None
        elif not head.next and stack:
            head.next = stack.pop()
            head.next.prev = head
        head = head.next
    return cur


# ---------------- Another solution without extra storage ------------


def flatten_2(head):
    if head is None:
        return

    curr = head
    while head:
        if head.child is None:
            head = head.next
            continue
        temp = head.child
        while temp.next:
            temp = temp.next
        if head.next:
            temp.next = head.next
            head.next.prev = temp
        head.next = head.child
        head.child.prev = head
        head.child = None
        head = head.next

    return curr
