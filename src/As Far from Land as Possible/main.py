from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: continue
                queue.append((row, col, 0))

        distances = [[-1] * len(grid[row]) for row in range(len(grid))]
        while queue:
            r, c, step = queue.popleft()
            print(r, c, step)
            if r - 1 >= 0 and grid[r - 1][c] == 0 and distances[r - 1][c] == -1:
                distances[r - 1][c] = step + 1
                queue.append((r - 1, c, step + 1))
            if r + 1 < len(grid) and grid[r + 1][c] == 0 and distances[r + 1][c] == -1:
                distances[r + 1][c] = step + 1
                queue.append((r + 1, c, step + 1))
            if c - 1 >= 0 and grid[r][c - 1] == 0 and distances[r][c - 1] == -1:
                distances[r][c - 1] = step + 1
                queue.append((r, c - 1, step + 1))
            if c + 1 < len(grid[0]) and grid[r][c + 1] == 0 and distances[r][c + 1] == -1:
                distances[r][c + 1] = step + 1
                queue.append((r, c + 1, step + 1))

        answer = -1
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                answer = max(answer, distances[row][col])
        return answer
