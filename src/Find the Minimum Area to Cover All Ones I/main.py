from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        has_one = False
        first_row = last_row = last_col = 0
        first_col = float("inf")

        for row in range(len(grid)):
            if 1 not in grid[row]: continue
            first_row = row
            has_one = True
            break

        if not has_one: return 0
        
        for row in range(len(grid) - 1, -1, -1):
            if 1 not in grid[row]: continue
            last_row = row
            break

        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == 0: continue
                first_col = min(first_col, col)
                last_col = max(last_col, col)

        print(last_row, first_row, last_col, first_col)
        return (last_row - first_row + 1) * (last_col - first_col + 1)