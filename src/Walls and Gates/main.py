from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] != 0: continue
                queue.append((row, col, 0))

        while queue:
            r, c, dist = queue.popleft()
            if r - 1 >= 0 and rooms[r - 1][c] == 2147483647:
                rooms[r - 1][c] = dist + 1
                queue.append((r - 1, c, dist + 1))
            if r + 1 < len(rooms) and rooms[r + 1][c] == 2147483647:
                rooms[r + 1][c] = dist + 1
                queue.append((r + 1, c, dist + 1))
            if c - 1 >= 0 and rooms[r][c - 1] == 2147483647:
                rooms[r][c - 1] = dist + 1
                queue.append((r, c - 1, dist + 1))
            if c + 1 < len(rooms[r]) and rooms[r][c + 1] == 2147483647:
                rooms[r][c + 1] = dist + 1
                queue.append((r, c + 1, dist + 1))
