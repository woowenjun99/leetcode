from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        dp[-1] = matrix[-1]
        for row in range(len(matrix) - 2, -1, -1):
            for col in range(len(matrix[0])):
                dp[row][col] = matrix[row][col] + min(
                    dp[row + 1][col - 1] if col - 1 >= 0 else float("inf"),
                    dp[row + 1][col],
                    dp[row + 1][col + 1] if col + 1 < len(matrix[0]) else float("inf")
                )
        return min(dp[0])