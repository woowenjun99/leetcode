from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        answer = temp = 0

        def dfs(grid, r, c):
            nonlocal temp
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0: return
            temp += grid[r][c]
            grid[r][c] = 0
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: continue
                temp = 0
                dfs(grid, row, col)
                answer = max(temp, answer)
        return answer
