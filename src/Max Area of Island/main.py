from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        current_area = maximum_area = 0

        def dfs(row, col):
            nonlocal current_area

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == 0: return
            grid[row][col] = 0
            current_area += 1

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: continue
                current_area = 0
                dfs(row, col)
                maximum_area = max(maximum_area, current_area)

        return maximum_area