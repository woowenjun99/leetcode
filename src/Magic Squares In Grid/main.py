from typing import List

class Solution:
    def __is_magical_subgrid__(self, subgrid: List[List[int]]) -> bool:
        # Check distinct numbers
        appeared = set()
        for row in range(3):
            for col in range(3):
                if subgrid[row][col] in appeared or subgrid[row][col] <= 0 or subgrid[row][col] > 9: return False
                appeared.add(subgrid[row][col])
    
        # Check row
        row_sum = []
        for row in range(3):
            total = 0
            for col in range(3): total += subgrid[row][col]
            row_sum.append(total)

        # Check col
        for col in range(3):
            total = 0
            for row in range(3): total += subgrid[row][col]
            row_sum.append(total)
        
        # Check diagonal
        row_sum.append(subgrid[0][0] + subgrid[1][1] + subgrid[2][2])
        row_sum.append(subgrid[0][2] + subgrid[1][1] + subgrid[2][0])
        return len(set(row_sum)) == 1

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        answer = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[row]) - 2):
                subgrid = [
                    [grid[row][col], grid[row][col + 1], grid[row][col + 2]],
                    [grid[row + 1][col], grid[row + 1][col + 1], grid[row + 1][col + 2]],
                    [grid[row + 2][col], grid[row + 2][col + 1], grid[row + 2][col + 2]]
                ]
                if self.__is_magical_subgrid__(subgrid):
                    answer += 1
        return answer