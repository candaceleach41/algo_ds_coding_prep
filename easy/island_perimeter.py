"""
You are given row x col grid representing a map where grid[i][j] = 1 represents
land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the
water around the island. One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of the
island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
"""


def island_perimeter(grid):
    rows, cols, border = len(grid), len(grid[0]), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    border += 1
                if c == 0 or grid[r][c - 1] == 0:
                    border += 1
                if c == cols - 1 or grid[r][c + 1] == 0:
                    border += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    border += 1
    return border
