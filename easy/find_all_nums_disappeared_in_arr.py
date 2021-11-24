"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an
array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]
"""


# Both solutions time and space complexity is O(n)
# n is the length of the array and using extra storage to store results
def find_disappeared_nums(nums):
    dic = {}
    for num in nums:
        dic[num] = 1

    result = []
    for num in range(1, len(nums) + 1):
        if num not in dic:
            result.append(num)
    return result


# ------------------------------------------
# Another solution using sets

def find_disappeared_nums_set(nums):
    set_nums = set(nums)
    result = []
    for num in range(1, len(nums) + 1):
        if num not in set_nums:
            result.append(num)
    return result
