"""
Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""


def reverse_words(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i][::-1]
    return " ".join(s)


# Found this solution on the discussion board
# This user used two pointer approach without using the split function
# Here's the link to this solution where the user explains it:
# https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/1051657/Python-3%3A-Two-pointer-approach-(for-the-sake-of-practice)

# Time: O(n) - n is the length of the string
# Space: O(n) - storing the results in a string
def reverse_words_2(s):
    result = ""
    left = 0
    right = 0

    while right < len(s):
        if s[right] != " ":
            right += 1
        elif s[right] == " ":
            result += s[left:right + 1][::-1]
            right += 1
            left = right
    result += " "
    result += s[left: right + 2][::-1]
    return result[1:]
