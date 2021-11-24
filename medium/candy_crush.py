"""
This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j]
represents the type of candy. A value of board[i][j] == 0 represents that the cell
is empty.

The given board represents the state of the game following the player's move. Now,
you need to restore the board to a stable state by crushing candies according to the
following rules:

If three or more candies of the same type are adjacent vertically or horizontally,
crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies
on top of itself, then these candies will drop until they hit a candy or bottom at
the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you
need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable),
then return the current board.
You need to perform the above rules until the board becomes stable, then return the
stable board.

Example 1:

Input: board = [
    [110,5,112,113,114],
    [210,211,5,213,214],
    [310,311,3,313,314],
    [410,411,412,5,414],
    [5,1,512,3,3],
    [610,4,1,613,614],
    [710,1,2,713,714],
    [810,1,2,1,1],
    [1,1,2,2,2],
    [4,1,4,4,1014]]

Output: [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [110,0,0,0,114],
    [210,0,0,0,214],
    [310,0,0,113,314],
    [410,0,0,213,414],
    [610,211,112,313,614],
    [710,311,412,613,714],
    [810,411,512,713,1014]]
"""


def candy_crush(board):
    rows, cols = len(board), len(board[0])
    stable = False
    while True:
        stable = True
        crushable = set()
        # 1. check for horizontal crushables
        for x in range(rows):
            for y in range(cols - 2):
                if board[x][y] == board[x][y + 1] == board[x][y + 2] != 0:
                    stable = False
                    crushable.update([(x, y), (x, y + 1), (x, y + 2)])

        # 2. check for vertical crushables
        for x in range(rows - 2):
            for y in range(cols):
                if board[x][y] == board[x + 1][y] == board[x + 2][y] != 0:
                    stable = False
                    crushable.update([(x, y), (x + 1, y), (x + 2, y)])

        # 5. if no candies were crushed, we're done
        if stable:
            return board

        # 3. crush the candies
        for x, y in crushable:
            board[x][y] = 0

        # 4. let the candies "fall"
        for y in range(cols):
            offset = 0
            for x in range(rows - 1, -1, -1):  # loop through column backward
                k = x + offset
                if (x, y) in crushable:  # this will help us put items at bottom of the board
                    offset += 1
                else:
                    board[k][y] = board[x][y]  # notice the use of k
            # now that all items have been copied to their right spots, place zero's appropriately at the top of the board
            for x in range(offset):
                board[x][y] = 0
