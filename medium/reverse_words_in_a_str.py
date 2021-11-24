"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include
any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in
the reversed string.

Example 4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
"""

from collections import deque


def reverse_words(string):
    left = 0
    right = len(string) - 1

    while left <= right and string[left] == " ":
        left += 1

    while left <= right and string[right] == " ":
        right -= 1

    word = []
    deque_word = deque()

    while left <= right:
        if string[left] == " " and word:
            deque_word.appendleft("".join(word))
            word = []
        elif string[left] != " ":
            word.append(string[left])
        left += 1

    deque_word.appendleft("".join(word))

    return " ".join(deque_word)
