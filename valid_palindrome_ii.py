"""
Given a string s, return true if the s can be palindrome after deleting at most one
character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


# Time: O(n)
# Space: O(1)
def valid_palindrome(s):
    def verify(s, left, right, deleted):
        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    return verify(s, left + 1, right, True) or verify(s, left, right - 1, True)
            else:
                left += 1
                right -= 1
        return True

    return verify(s, 0, len(s) - 1, False)


# Another Solution ---------------------------------------------------------------------------
# Time: O(n)
# Space: O(1)
def valid_palindrome_v2(s):
    low = 0
    high = len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return is_palindrome(s, low + 1, high) or is_palindrome(s, low, high - 1)
        low += 1
        high -= 1


def is_palindrome(string, low, high):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


if __name__ == "__main__":
    print(valid_palindrome_v2("abcba"))
