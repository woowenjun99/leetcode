from typing import List

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        col = -1
        is_skipped = False
        answer = []
        for row in range(len(grid)):
            if col == -1:
                col += 1
                while col < len(grid[row]):
                    if not is_skipped: answer.append(grid[row][col])
                    is_skipped = not is_skipped
                    col += 1
            else:
                col -= 1
                while col >= 0:
                    if not is_skipped: answer.append(grid[row][col])
                    is_skipped = not is_skipped
                    col -= 1
        return answer