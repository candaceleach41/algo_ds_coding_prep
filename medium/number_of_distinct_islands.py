"""
You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You may
assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be
translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.



Example 1:


Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1
Example 2:


Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3
"""


def numDistinctIslands(self, grid):
    def dfs(start, shape, row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
            shape.append((row - start[0], col - start[1]))
            grid[row][col] = 0
            dfs(start, shape, row + 1, col)
            dfs(start, shape, row - 1, col)
            dfs(start, shape, row, col + 1)
            dfs(start, shape, row, col - 1)
        return shape

    unique_islands = set()
    islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                island = tuple(dfs((row, col), [], row, col))
                if island not in unique_islands:
                    unique_islands.add(island)
                    islands += 1
    return islands