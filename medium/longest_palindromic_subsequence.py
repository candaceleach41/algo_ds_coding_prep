"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting
some or no elements without changing the order of the remaining elements.


Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


# Time: O(mn) - m is row and n is col
# Space: O(mn)
def longest_palindrome_subseq(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for k in range(1, len(s) + 1):
        for i in range(len(s) - k + 1):
            j = k + i - 1
            if i == j:
                dp[i][j] = 1
            elif i + 1 == j and s[i] == s[j]:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][-1]


if __name__ == "__main__":
    print(longest_palindrome_subseq("bbbab"))
