"""
Given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""


# Time: O(n log n) - because of sorting
# Space: O(1) - no additional space used
def sorted_squares(nums):
    for i in range(len(nums)):
        nums[i] *= nums[i]
    # nums.sort()
    # return nums
    return sorted(nums)  # Added after comparing my solution to an optimal one


# ----------------------------------------------
# Another Solution (using two pointers)
# Time: O(n)
# Space: O(n)
def sqrt_sorted_arr(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result
