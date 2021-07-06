"""
You are given a string s. We want to partition the string into as many parts as possible
so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into
less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]
"""


# Time and Space: O(n) - n is the number of characters and using extra storage
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    start = 0
    end = 0
    result = []

    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result
