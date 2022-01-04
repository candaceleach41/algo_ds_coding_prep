"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest
number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""


# Using binary search
def kth_smallest(matrix, k):
    n, left, right = len(matrix), matrix[0][0], matrix[-1][-1]

    def check(m):
        i, j, count = 0, n - 1, 0
        for i in range(n):
            while j >= 0 and matrix[i][j] > m:
                j -= 1
            count += (j + 1)
        return count

    while left < right:
        mid = (left + right) // 2
        if check(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left


# -------------------- Another solution using heap -------------
from typing import List
from heapq import heappush, heappushpop


def kth_smallest_heap(self, matrix: List[List[int]], k: int) -> int:
    if not matrix or not matrix[0]:
        return -1

    heap = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            next_val = -matrix[row][col]
            if len(heap) < k:
                heappush(heap, next_val)
            elif next_val > heap[0]:
                heappushpop(heap, next_val)
    return -heap[0]
