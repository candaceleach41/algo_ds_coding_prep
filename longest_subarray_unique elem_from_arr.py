"""
Given an array arr[] consisting of N integers, the task is to find the largest subarray
consisting of unique elements only.

Examples:
Input: arr[] = {1, 2, 3, 4, 5, 1, 2, 3}
Output: 5
Explanation: One possible subarray is {1, 2, 3, 4, 5}.

Input: arr[]={1, 2, 4, 4, 5, 6, 7, 8, 3, 4, 5, 3, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4}
Output: 8
Explanation: Only possible subarray is {3, 4, 5, 6, 7, 8, 1, 2}.
"""


# Using sliding window approach
# Time: O(n) - n is the length of the arr
# Space: O(n) using extra space to store elems that have been seen
def length_of_longest_substring(arr):
    seen = {}
    left = 0
    res = 0
    for right in range(len(arr)):
        if arr[right] not in seen:
            res = max(res, right - left + 1)
        else:
            if seen[arr[right]] < left:
                res = max(res, right - left + 1)
            else:
                # shrink the left side of the window
                left = seen[arr[right]] + 1
        # increase the right side of the window
        seen[arr[right]] = right
    return res
