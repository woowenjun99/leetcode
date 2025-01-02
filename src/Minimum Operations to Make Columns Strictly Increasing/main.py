from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        answer = 0
        for col in range(len(grid[0])):
            for row in range(1, len(grid)):
                if grid[row][col] > grid[row - 1][col]: continue
                answer += grid[row - 1][col] - grid[row][col] + 1
                grid[row][col] = grid[row - 1][col] + 1
        return answer
