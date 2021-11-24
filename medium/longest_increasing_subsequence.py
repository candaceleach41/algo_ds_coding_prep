"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no
elements without changing the order of the remaining elements. For example, [3,6,2,7]
is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

# Using dynamic programming
def length_of_lis(nums):
    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


# Using dynamic programming and binary search
def length_of_lis_bs(nums):
    tails = [0] * len(nums)
    size = 0
    for k in nums:
        i, j = 0, size
        while i != j:
            mid = (i + j) / 2
            if tails[mid] < k:
                i = mid + 1
            else:
                j = mid
        tails[i] = k
        size = max(i + 1, size)
    return size
