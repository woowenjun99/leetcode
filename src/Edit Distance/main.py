class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Initialising the base case
        dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        dp[-1][-1] = 0
        for col in range(m - 1, -1, -1): dp[-1][col] = 1 + dp[-1][col + 1]
        for row in range(n - 1, -1, -1): dp[row][-1] = 1 + dp[row + 1][-1]
        
        # Perform the calculation
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if word2[row] == word1[col]:
                    dp[row][col] = dp[row + 1][col + 1]
                else:
                    dp[row][col] = 1 + min(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1])
        return dp[0][0]