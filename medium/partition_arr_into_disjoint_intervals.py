"""
Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.

Example 1:
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
"""


def partition_disjoint(nums):
    left_max = nums[0]
    overall_max = nums[0]
    pivot = 0
    for i, n in enumerate(nums):
        if n < left_max:
            pivot = i
            left_max = overall_max
        elif n > overall_max:
            overall_max = n
    return pivot + 1

