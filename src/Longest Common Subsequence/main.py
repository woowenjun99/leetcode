class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if text1[col] == text2[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                    continue
                dp[row][col] = max(dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1])
        return dp[0][0]