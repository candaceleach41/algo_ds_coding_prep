"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""


# Using sliding window approach
# Time: O(n)
# Space: O(n)
def length_of_longest_substring(self, s):
    seen = {}
    left = 0
    res = 0
    for right in range(len(s)):
        if s[right] not in seen:
            res = max(res, right - left + 1)
        else:
            if seen[s[right]] < left:
                res = max(res, right - left + 1)
            else:
                left = seen[s[right]] + 1
        seen[s[right]] = right
    return res
