"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

# Time: O(n+m) - n is nums1 and m is nums2
# Space: O(n) - using extra space
def intersection(nums1, nums2):
    dic = {}
    result = []
    for num in nums1:
        dic[num] = 1

    for num in nums2:
        if num in dic and dic[num]:
            result.append(num)
            dic[num] -= 1

    return result


# ------------------------------
# Another solution using sets
def intersection_set(nums1, nums2):
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    print(intersection_set([4, 9, 5], [9, 4, 9, 8, 4]))
