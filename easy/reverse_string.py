"""
Write a function that reverses a string. The input string is given as an
array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Problem also said not to return anything
"""


# Time: O(n) - where n is length of the string
# Space: O(1) - Not adding additional space

# Would not use this solution during an interview, but could talk about it
def reverse_string_1(s):
    s.reverse()


# Time: O(n) - where n is length of the string
# Space: O(1) - Not adding additional space since we're swapping strings inplace

# Using two pointers
def reverse_string_2(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

