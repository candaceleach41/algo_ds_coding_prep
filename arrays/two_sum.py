"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


# Worst Case (Time: O(n^2) | Space O(1)
# This is using nested for loop
def two_sum_wc(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
            j += 1
        i += 1
    return []


# A bit of improvement from the problem above
# When the array is sorted (Time: O(n log n) | Space O(1)
def two_sum_sorted(arr, target):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] + arr[i+1] == target:
            return i, i+1
        i += 1
    return []


# Optimized solution using dictionary
# Time O(1) | Space O(1)
def two_sum_dict(arr, target):
    visited = {}
    for i, num in enumerate(arr):
        if num in visited:
            return visited[num], i
        visited[target - num] = i
    return []


if __name__ == "__main__":
    print("Worst Case:", two_sum_wc([2, 7, 8, 3], 9))
    print("Sorted array:", two_sum_sorted([7, 3, 6, 1, 4], 10))
    print("Using a dictionary:", two_sum_dict([4, 1, 8, 4, 6, 5], 14))
    