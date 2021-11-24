"""
Given an integer array nums, return the number of triplets chosen from the array that
can make triangles if we take them as side lengths of a triangle.

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""


def triangle_number(nums):
    n = len(nums)
    nums.sort()
    count = 0

    for i in range(2, n):
        curr_num = nums[i]
        left = 0
        right = i - 1

        while left < right:
            left_num = nums[left]
            right_num = nums[right]

            if left_num + right_num > curr_num:
                count += right - left
                right -= 1
            else:
                left += 1

    return count
