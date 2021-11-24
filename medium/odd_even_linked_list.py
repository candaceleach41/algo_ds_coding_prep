"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the
nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.



Example 1:

            1 -> 2 -> 3 -> 4 -> 5
                      |
                      v
            1 -> 3 -> 5 -> 2 -> 4

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

            2 -> 1 -> 3 -> 5 -> 6 -> 4 -> 7
                           |
                           v
            2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


""" Note: I am adding the append function so I don't have to keep typing .next for each node
manually. The solution to this problem is below the append function"""


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # ------------ The function below is the coding problem --------------------------------

    def odd_even_list(self, head):
        if not self.head:
            return self.head

        odd = self.head
        even = self.head.next
        even_head = even

        while even and odd and even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return self.head


if __name__ == "__main__":
    node = LinkedList()
    node.append(2)
    node.append(1)
    node.append(3)
    node.append(5)
    node.append(6)
    node.append(4)
    node.append(7)
    node.print_list()
    # print(node.odd_even_list(node))
