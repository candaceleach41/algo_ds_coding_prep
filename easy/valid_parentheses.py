"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""


def is_valid(s):
    open_brackets = ["(", "{", "["]
    closed_brackets = [")", "}", "]"]
    stack = []

    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in closed_brackets:
            if len(stack) <= 0:
                return False
            if open_brackets.index(stack.pop()) != closed_brackets.index(bracket):
                return False
    return len(stack) == 0


# Using dictionary
def is_valid_dict(s):
    stack = []
    brackets = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or brackets[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


if __name__ == "__main__":
    print(is_valid("()"))  # True
    print(is_valid("(){)"))  # False
    print(is_valid_dict("{}"))  # True
    print(is_valid_dict("{[()]}"))  # True
    print(is_valid_dict("{[(})]"))  # False
