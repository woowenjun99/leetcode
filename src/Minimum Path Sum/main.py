class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        for column in range(len(grid[-1]) - 2, -1, -1): dp[-1][column] = dp[-1][column + 1] + grid[-1][column]
        for row in range(len(grid) - 2, -1, -1): dp[row][-1] = grid[row][-1] + dp[row + 1][-1]

        for row in range(len(grid) - 2, -1, -1):
            for column in range(len(grid[0]) - 2, -1, -1):
                dp[row][column] = grid[row][column] + min(dp[row + 1][column], dp[row][column + 1])

        return dp[0][0]