"""
Given a string s and a character c that occurs in s, return an array of integers answer
where answer.length == s.length and answer[i] is the distance from index i to the closest
occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value
function.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 3.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the
distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
"""


# Time and space: O(n) - n is the length of the s and using extra storage
def shortest_to_char(s, c):
    length = len(s)
    pos = float("-inf")
    result = [length] * length
    for i in list(range(length)) + list(range(length)[::-1]):
        if s[i] == c:
            pos = i
        result[i] = min(result[i], abs(i - pos))
    return result


# ----------------------------Another solution using DP--------------
def shortest_to_chr_dp(s, c):
    length = len(s)
    result = [0 if ch == c else length for ch in s]
    for i in range(1, length):
        result[i] = min(result[i], result[i - 1] + 1)
    for i in range(length - 2, -1, -1):
        result[i] = min(result[i], result[i + 1] + 1)
    return result
