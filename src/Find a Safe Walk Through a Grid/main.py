from collections import deque
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        distances = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        distances[0][0] = grid[0][0]
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for direction in DIRECTIONS:
                if row + direction[0] >= 0 and row + direction[0] < len(grid) and col + direction[1] >= 0 and col + direction[1] < len(grid[0]):
                    if distances[row + direction[0]][col + direction[1]] == float("inf"):
                        distances[row + direction[0]][col + direction[1]] = distances[row][col] + grid[row + direction[0]][col + direction[1]]
                        if grid[row + direction[0]][col + direction[1]] == 0: queue.appendleft((row + direction[0], col + direction[1]))
                        else: queue.append((row + direction[0], col + direction[1]))
        return distances[-1][-1] < health
