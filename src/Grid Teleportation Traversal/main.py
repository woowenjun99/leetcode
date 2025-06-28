from collections import deque, defaultdict
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        # Step 1: Add in all the portals
        portals = defaultdict(list)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != "#" and matrix[row][col] != ".":
                    portals[matrix[row][col]].append((row, col))

        distances = [[float("inf")] * len(matrix[0]) for _ in range(len(matrix))]
        distances[0][0] = 0
        queue = deque([(0, 0, 0)])
        if matrix[0][0] in portals:
            for portal in portals[matrix[0][0]]:
                queue.append((portal[0], portal[1], 0))
                distances[portal[0]][portal[1]] = 0

        while queue:
            r, c, d = queue.popleft()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for x, y in directions:
                if not (0 <= r + x < len(matrix) and 0 <= c + y < len(matrix[0])): continue
                if distances[r + x][c + y] != float("inf") or matrix[r + x][c + y] == "#": continue
                if matrix[r + x][c + y] in portals:
                    for portal in portals[matrix[r + x][c + y]]:
                        distances[portal[0]][portal[1]] = d + 1
                        queue.append((portal[0], portal[1], d + 1))
                    continue
                distances[r + x][c + y] = d + 1
                queue.append((r + x, c + y, d + 1))

        return -1 if distances[-1][-1] == float("inf") else distances[-1][-1]