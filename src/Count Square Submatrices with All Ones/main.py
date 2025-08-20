from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for col in range(len(matrix[0])): dp[0][col] = matrix[0][col]
        for row in range(len(matrix)): dp[row][0] = matrix[row][0]

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0: continue
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1

        answer = 0
        for row in dp: answer += sum(row)
        return answer