"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

                    1  ->  2  ->  3
                                  |
                                  v
                    4  ->  5      6
                    ^             |
                    |             v
                    7  <-  8  <-  9


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

                    1 ->  2 ->  3 ->  4
                                      |
                                      v
                    5  -> 6 ->  7     8
                    ^                 |
                    |                 v
                    9  <- 10 <- 11 <- 12

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def spiral_order(matrix):
    result = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)

    while left < right and top < bottom:
        # get every i in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # get every i in the right col
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        # get every i in the bottom row
        for i in range(right - 1, left - 1, -1):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every i in the left col
        for i in range(bottom - 1, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result
