"""
Given two equal-size strings s and t. In one step you can choose any character of t and
replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different
(or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t
anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.
"""

from collections import defaultdict


def min_steps(s, t):
    memo = defaultdict(int)
    for char in s:
        memo[char] += 1

    count = 0
    for char in t:
        if memo[char]:
            memo[char] -= 1
        else:
            count += 1

    return count


# ----------------- Another Solution using set -------------------
def min_steps_ii(s, t):
    steps = 0
    for char in set(s):
        count_s = s.count(char)
        count_t = t.count(char)
        if count_s > count_t:
            steps += count_s - count_t

    return steps
