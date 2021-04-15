"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string is valid
and return any valid string.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are
  valid strings, or
- It can be written as (A), where A is a valid string.


Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""


# time: O(n)
# space: O(n)
def min_remove_valid_paren(string):
    string = list(string)
    stack = []

    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                string[i] = ''

    while stack:
        string[stack.pop()] = ''
    return ''.join(string)


if __name__ == "__main__":
    print(min_remove_valid_paren("lee(t(c)o)de)"))  # lee(t(c)o)de
    print(min_remove_valid_paren("a)b(c)d"))  # ab(c)d
