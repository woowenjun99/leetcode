from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        answer = max_diagonal = 0
        for row, col in dimensions:
            if row * row + col * col > max_diagonal:
                max_diagonal = row * row + col * col
                answer = row * col
            elif row * row + col * col == max_diagonal:
                answer = max(answer, row * col)
        return answer