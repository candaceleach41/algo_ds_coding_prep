"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    s = s.lower()
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        elif not s[right].isalnum():
            right -= 1
            continue
        elif s[left].isalnum() == True and s[right].isalnum() == True:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
    return True


# ------------------------------- Similar to above solution, just shorter -------------
def is_palindrome_v2(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
