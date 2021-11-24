"""
(This problem is an interactive problem.)

A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix
is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the
leftmost column with a 1 in it. If such an index does not exist, return -1.

You can't access the Binary Matrix directly. You may only access the matrix using a
BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements
[rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes, the input will be the entire binary matrix mat. You will not
have access to the binary matrix directly.

Example 1:
    --------------
    |   0  |  0  |
    --------------
    |  1  |  1  |
    -------------
       ^
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:

    --------------
    |   0  |  0  |
    --------------
    |  1  |  1  |
    -------------
            ^
Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:


Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """


# Using binary search
# Time: O(nm) n is the row and m is the column
# Space: O(1) not using extra space
def leftMostColumnWithOne(binaryMatrix):
    rows, cols = binaryMatrix.dimensions()
    left = 0
    right = cols - 1

    while left <= right:
        mid = (left + right) // 2
        seen = any([binaryMatrix.get(r, mid) for r in range(rows)])

        if left == right:
            return -1 if not seen else left

        if seen:
            right = mid
        else:
            left = mid + 1
