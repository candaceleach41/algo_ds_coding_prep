"""
Given a string s consists of some words separated by spaces, return the length of the last
word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
"""


def length_of_last_word(s):
    result = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            result += 1
        elif result:
            return result

    return result
