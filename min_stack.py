"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""


class MinStack:
    def __init__(self) -> object:
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def get_min(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


if __name__ == "__main__":
    ms = MinStack()
    print("Push", ms.push(-2))
    print("Push", ms.push(0))
    print("Push", ms.push(-3))
    print("Get Min", ms.get_min())
    print(ms.pop())
    print(ms.top())
    print("Get Min", ms.get_min())

