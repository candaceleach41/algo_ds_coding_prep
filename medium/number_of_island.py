"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's
 (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


def numIslands(grid):
    if not grid:
        return 0

    num_of_island = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                dfs(grid, row, col)
                num_of_island += 1
    return num_of_island


def dfs(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1":
        return 0

    grid[row][col] = "2"
    dfs(grid, row + 1, col)  # Down
    dfs(grid, row - 1, col)  # Up
    dfs(grid, row, col + 1)  # Right
    dfs(grid, row, col - 1)  # Left

