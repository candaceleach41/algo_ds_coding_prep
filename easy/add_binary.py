"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


# Time: O(nm) - n is the length of a and m is the length of b
# Space: O(n) - using extra space to store the result
def add_binary(a, b):
    res = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while carry or i >= 0 or j >= 0:
        total = carry
        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1
        res.append(str(total % 2))
        carry = total // 2
    return "".join(res[::-1])
