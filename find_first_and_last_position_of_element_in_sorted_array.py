"""
Given an array of integers nums sorted in ascending order, find the starting and ending
position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""


# Time: O(log n) - using two binary search
# Space: O(1) - no extra storage
def search_range(nums, target):
    low, high = 0, len(nums) - 1
    first = find_first_idx(nums, low, high, target)
    second = find_last_idx(nums, low, high, target)


def find_first_idx(nums, low, high, target):
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return res


def find_last_idx(nums, low, high, target):
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return res
