"""
Given an array nums of distinct integers, return all the possible permutations. You can
return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""


def permute(nums):
    visited = set()
    result = []
    backtracking(result, visited, [], nums)
    return result


def backtracking(result, visited, subset, nums):
    if len(subset) == len(nums):
        result.append(subset)

    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(result, visited, subset + [nums[i]], nums)
            visited.remove(i)
