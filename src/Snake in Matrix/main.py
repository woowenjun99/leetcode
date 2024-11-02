from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        grid = [[0] * n for _ in range(n)]
        row = col = count = 0

        for i in range(n):
            for j in range(n):
                grid[i][j] = count
                count += 1
        
        for command in commands:
            if command == "UP": row -= 1
            elif command == "DOWN": row += 1
            elif command == "LEFT": col -= 1
            else: col += 1
        return grid[row][col]