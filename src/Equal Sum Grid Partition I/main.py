from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        for row in range(len(grid)):
            current = 0
            for col in range(len(grid[0])): current += grid[row][col]
            rows[row] = current

        for col in range(len(grid[0])):
            current = 0
            for row in range(len(grid)): current += grid[row][col]
            cols[col] = current

        left = rows[0]
        right = sum(rows) - rows[0]
        for i in range(len(rows) - 1):
            if left == right: return True
            left += rows[i + 1]
            right -= rows[i + 1]

        left = cols[0]
        right = sum(cols) - cols[0]
        for i in range(len(cols) - 1):
            if left == right: return True
            left += cols[i + 1]
            right -= cols[i + 1]
        return False