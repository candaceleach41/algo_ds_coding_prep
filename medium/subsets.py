"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


def subsets(nums):
    result = []
    backtracking(result, 0, [], nums)
    return result


def backtracking(result, start, subset, nums):
    result.append(list(subset))
    for i in range(start, len(nums)):
        subset.append(nums[i])
        backtracking(result, i + 1, subset, nums)
        subset.pop()
