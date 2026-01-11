from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = num_negatives = 0
        smallest_num = float("inf")
        contains_zero = False
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                total += abs(matrix[row][col])
                if matrix[row][col] < 0: num_negatives += 1
                elif matrix[row][col] == 0: contains_zero = True
                smallest_num = min(abs(matrix[row][col]), smallest_num)

        if num_negatives % 2 == 0 or contains_zero: return total
        return total - 2 * smallest_num