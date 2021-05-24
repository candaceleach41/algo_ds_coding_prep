"""
Given an array of integers nums and an integer k, return the total number of continuous
subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""


# Brute force approach
# Time: O(n^3)
# Space: O(1)

def subarray_sum(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j + 1]) == k:
                count += 1
    return count


# using prefix sum
# Time: O(n^2)
# Space: O(1)
def subarray_sum_2(nums, k):
    if not nums:
        return 0
    if len(nums) == 1:
        if nums[0] == k:
            return 1
        return 0

    # Build prefix sum:
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    nums.insert(0, 0)

    # itertate over prefix sum and see
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] - nums[i] == k:
                count += 1
    return count


# Using Hash Table
# Time: O(n)
# Space: O(n)
def subarray_sum_ht(nums, k):
    dic = {0: 1}
    s = 0
    count = 0
    for i in range(len(nums)):
        s += nums[i]
        if s - k in dic:
            count += dic[s - k]
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    return count
