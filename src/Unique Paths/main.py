class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for column in range(n): dp[-1][column] = 1
        for row in range(m): dp[row][-1] = 1
        for row in range(m - 2, -1, -1):
            for column in range(n - 2, -1, -1):
                dp[row][column] = dp[row + 1][column] + dp[row][column + 1]
        return dp[0][0]