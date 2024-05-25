from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        exits = set()
        for row in range(len(maze)):
            if maze[row][0] == ".": exits.add((row, 0))
            if maze[row][-1] == ".": exits.add((row, len(maze[row]) - 1))
        for column in range(len(maze[0])):
            if maze[0][column] == ".": exits.add((0, column))
            if maze[-1][column] == ".": exits.add((len(maze) - 1, column))
        if (entrance[0], entrance[1]) in exits: exits.remove((entrance[0], entrance[1]))
        
        visited = [[False] * len(maze[0]) for _ in range(len(maze))]
        queue = deque([(entrance[0], entrance[1], 0)])
        while queue:
            row, col, step = queue.popleft()
            if row - 1 >= 0 and not visited[row - 1][col]:
                visited[row - 1][col] = True
                if (row - 1, col) in exits: return step + 1
                if maze[row - 1][col] == ".": queue.append((row - 1, col, step + 1))
            if row + 1 < len(maze) and not visited[row + 1][col]:
                visited[row + 1][col] = True
                if (row + 1, col) in exits: return step + 1
                if maze[row + 1][col] == ".": queue.append((row + 1, col, step + 1))
            if col - 1 >= 0 and not visited[row][col - 1]:
                visited[row][col - 1] = True
                if (row, col - 1) in exits: return step + 1
                if maze[row][col - 1] == ".": queue.append((row, col - 1, step + 1))
            if col + 1 < len(maze[0]) and not visited[row][col + 1]:
                visited[row][col + 1] = True
                if (row, col + 1) in exits: return step + 1
                if maze[row][col + 1] == ".": queue.append((row, col + 1, step + 1))
        return -1