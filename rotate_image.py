"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
(clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix
directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

                        1   2   3                   7   4   1
                        4   5   6     ------>       8   5   2
                        7   8   9                   9   6   3


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

                5   1   9   11                  15  13  2   5
                2   4   8   10                  14  3   4   1
                13  3   6   7     ------->      12  6   8   9
                15  14  12  16                  16  7   10  11


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    left = 0
    right = len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top = left
            bottom = right

            # Save the top left as a temp variable
            top_left = matrix[top][left + i]

            # Move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move top right into bottom right
            matrix[bottom][right - i] = matrix[top - i][right]

            # Move top left into top right
            matrix[top + i][right] = top_left

        right -= 1
        left += 1
