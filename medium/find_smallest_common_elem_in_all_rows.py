"""
Given an m x n matrix mat where every row is sorted in strictly increasing order,
return the smallest common element in all rows.

If there is no common element, return -1.


Example 1:
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

Example 2:
Input: mat = [[1,2,3],[2,3,4],[2,3,5]]
Output: 2
"""
import collections


# Using dictionary
# Time: O(mn) - m is the num of rows and n is the num of column
# Space: O(1)
def smallest_common_elem(mat):
    common_elem = collections.defaultdict(int)
    for arr in mat:
        for num in arr:
            common_elem[num] += 1
            if common_elem[num] == len(mat):
                return num
    return -1


# binary search
# Time: O(nm logn)
# Space: O(1)
def smallest_common_elem_2(mat):
    def binary_search(val, arr):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if val == arr[mid]:
                return 1
            elif val >= arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return 0

    for num in mat[0]:
        for arr in mat[1:]:
            if not binary_search(num, arr):
                break
        else:
            return num
    return -1
