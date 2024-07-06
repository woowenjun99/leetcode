from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        time_elapsed = 0
        while queue:
            row, col, duration = queue.popleft()
            time_elapsed = duration
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                grid[row - 1][col] = 2
                queue.append((row - 1, col, duration + 1))
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                grid[row + 1][col] = 2
                queue.append((row + 1, col, duration + 1))
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                grid[row][col - 1] = 2
                queue.append((row, col - 1, duration + 1))
            if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                grid[row][col + 1] = 2
                queue.append((row, col + 1, duration + 1))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    return -1
        return time_elapsed