"""
A permutation perm of n + 1 integers of all the integers in the range [0, n]
can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are
multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]
"""


def di_string_match(string):
    result = []
    str_i = 0
    str_d = len(string)

    for x in string:
        if x == "I":
            result.append(str_i)
            str_i += 1
        elif x == "D":
            result.append(str_d)
            str_d -= 1
    result.append(str_i)
    return result
