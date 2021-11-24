"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:


Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""


def max_area_of_island(grid):
    row = len(grid)
    col = len(grid[0])
    max_area = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                stack = list()
                area = 0
                stack.append((i, j))
                grid[i][j] = 0
                while len(stack) > 0:
                    x, y = stack.pop()
                    area += 1
                    if x > 0 and grid[x - 1][y] == 1:
                        stack.append((x - 1, y))
                        grid[x - 1][y] = 0
                    if y > 0 and grid[x][y - 1] == 1:
                        stack.append((x, y - 1))
                        grid[x][y - 1] = 0
                    if x < row - 1 and grid[x + 1][y] == 1:
                        stack.append((x + 1, y))
                        grid[x + 1][y] = 0
                    if y < col - 1 and grid[x][y + 1] == 1:
                        stack.append((x, y + 1))
                        grid[x][y + 1] = 0
                max_area = max(max_area, area)
    return max_area


if __name__ == "__main__":
    print(max_area_of_island([
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]))
