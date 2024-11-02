from typing import List

class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.mappers = {}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.mappers[grid[row][col]] = (row, col)

    def adjacentSum(self, value: int) -> int:
        row, col = self.mappers[value]
        up = 0 if row - 1 < 0 else self.grid[row - 1][col]
        down = 0 if row + 1 >= len(self.grid) else self.grid[row + 1][col]
        left = 0 if col - 1 < 0 else self.grid[row][col - 1]
        right = 0 if col + 1 >= len(self.grid[0]) else self.grid[row][col + 1]
        return up + down + left + right

    def diagonalSum(self, value: int) -> int:
        row, col = self.mappers[value]
        up = 0 if (row - 1 < 0 or col - 1 < 0) else self.grid[row - 1][col - 1]
        down = 0 if (row + 1 >= len(self.grid) or col + 1 >= len(self.grid[0])) else self.grid[row + 1][col + 1]
        left = 0 if (row + 1 >= len(self.grid) or col - 1 < 0) else self.grid[row + 1][col - 1]
        right = 0 if (row - 1 < 0 or col + 1 >= len(self.grid[0])) else self.grid[row - 1][col + 1]
        return up + down + left + right