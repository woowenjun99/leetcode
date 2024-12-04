from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 0)])
        distances = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        distances[0][0] = 0
        while queue:
            row, col, distance = queue.popleft()
            if 0 <= row - 1 and distance + grid[row - 1][col] < distances[row - 1][col]:
                distances[row - 1][col] = distance + grid[row - 1][col]
                if grid[row - 1][col] == 1: queue.append((row - 1, col, distance + 1))
                else: queue.appendleft((row - 1, col, distance))
            if row + 1 < len(grid) and distance + grid[row + 1][col] < distances[row + 1][col]:
                distances[row + 1][col] = distance + grid[row + 1][col]
                if grid[row + 1][col] == 1: queue.append((row + 1, col, distance + 1))
                else: queue.appendleft((row + 1, col, distance))
            if col - 1 >= 0 and distance + grid[row][col - 1] < distances[row][col - 1]:
                distances[row][col - 1] = distance + grid[row][col - 1]
                if grid[row][col - 1] == 1: queue.append((row, col - 1, distance + 1))
                else: queue.appendleft((row, col - 1, distance))
            if col + 1 < len(grid[0]) and distance + grid[row][col + 1] < distances[row][col + 1]:
                distances[row][col + 1] = distance + grid[row][col + 1]
                if grid[row][col + 1] == 1: queue.append((row, col + 1, distance + 1))
                else: queue.appendleft((row, col + 1, distance))
        return distances[-1][-1]
