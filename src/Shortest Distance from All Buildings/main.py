from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        housing_id = 0
        distances = [[0] * len(grid[0]) for _ in range(len(grid))]
        visited = defaultdict(set)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 1: continue
                queue.append((row, col, housing_id, 0))
                housing_id += 1
                distances[row][col] = 0
                visited[(row, col)].add(housing_id)

        while queue:
            r, c, jd, dist = queue.popleft()
            if r - 1 >= 0 and jd not in visited[(r - 1, c)]:
                visited[(r - 1, c)].add(jd)
                if grid[r - 1][c] == 0:
                    distances[r - 1][c] += dist + 1
                    queue.append((r - 1, c, jd, dist + 1))
            if r + 1 < len(grid) and jd not in visited[(r + 1, c)]:
                visited[(r + 1, c)].add(jd)
                if grid[r + 1][c] == 0:
                    distances[r + 1][c] += dist + 1
                    queue.append((r + 1, c, jd, dist + 1))
            if c - 1 >= 0 and jd not in visited[(r, c - 1)]:
                visited[(r, c - 1)].add(jd)
                if grid[r][c - 1] == 0:
                    distances[r][c - 1] += dist + 1
                    queue.append((r, c - 1, jd, dist + 1))
            if c + 1 < len(grid[0]) and jd not in visited[(r, c + 1)]:
                visited[(r, c + 1)].add(jd)
                if grid[r][c + 1] == 0:
                    distances[r][c + 1] += dist + 1
                    queue.append((r, c + 1, jd, dist + 1))

        answer = float("inf")
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 0 or len(visited[(row, col)]) != housing_id: continue
                answer = min(distances[row][col], answer)
        return answer if answer != float("inf") else -1