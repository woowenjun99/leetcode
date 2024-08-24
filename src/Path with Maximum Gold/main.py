from typing import List

class Solution:
    def backtracking(self, row, col, current_gold, visited, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]): return current_gold
        if grid[row][col] == 0 or visited[row][col]: return current_gold
        visited[row][col] = True
        up = self.backtracking(row - 1, col, current_gold + grid[row][col], visited, grid)
        down = self.backtracking(row + 1, col, current_gold + grid[row][col], visited, grid)
        left = self.backtracking(row, col - 1, current_gold + grid[row][col], visited, grid)
        right = self.backtracking(row, col + 1, current_gold + grid[row][col], visited, grid)
        visited[row][col] = False
        return max(up, down, left, right)

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: continue
                visited = [[False] * len(grid[row]) for _ in range(len(grid))]
                answer = max(answer, self.backtracking(row, col, 0, visited, grid))
        return answer