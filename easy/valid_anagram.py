"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""


# Time: O(n)
# Space: O(n)
def is_anagram(s, t):
    # If both s and t does not have the same length, return False
    if len(s) != len(t):
        return False

    # Use a dictionary to store the chars
    letters = {}
    for char in s:
        if char not in letters:
            letters[char] = 0
        letters[char] += 1

    for char in t:
        if char not in letters or letters[char] < 1:
            return False
        letters[char] -= 1

    return True


# ------------------ Another solution using set ------------------------

# Time: O(n)
# Space: O(1)
def is_anagram_set(s, t):
    if set(s) != set(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True
