"""
Given an array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size
2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use
the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
"""

# Binary Search Approach
# Time: O(log n)
# Space: O(1)

def two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum_nums = nums[left] + nums[right]
        if sum_nums == target:
            return [left + 1, right + 1]
        elif sum_nums < target:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
