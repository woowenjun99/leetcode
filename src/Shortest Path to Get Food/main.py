from collections import deque
from typing import List

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        distances = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != "*": continue
                queue.append((row, col, 0))
                distances[row][col] = 0
                break
        
        while queue:
            row, col, dist = queue.popleft()
            if grid[row][col] == "#": return dist
            if row >= 1 and grid[row - 1][col] != "X" and distances[row - 1][col] == float("inf"):
                distances[row - 1][col] = dist + 1
                queue.append((row - 1, col, dist + 1))
            if row < len(grid) - 1 and grid[row + 1][col] != "X" and distances[row + 1][col] == float("inf"):
                distances[row + 1][col] = dist + 1
                queue.append((row + 1, col, dist + 1))
            if col - 1 >= 0 and grid[row][col - 1] != "X" and distances[row][col - 1] == float("inf"):
                distances[row][col - 1] = dist + 1
                queue.append((row, col - 1, dist + 1))
            if col < len(grid[0]) - 1 and grid[row][col + 1] != "X" and distances[row][col + 1] == float("inf"):
                distances[row][col + 1] = dist + 1
                queue.append((row, col + 1, dist + 1))
        return -1