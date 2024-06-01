class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Build the DP graph
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        has_obstacle_in_last_row = False
        for col in range(len(obstacleGrid[0]) - 1, -1, -1):
            if obstacleGrid[-1][col] == 1: has_obstacle_in_last_row = True
            if has_obstacle_in_last_row: continue
            dp[-1][col] = 1
        has_obstacle_in_last_col = False
        for row in range(len(obstacleGrid) - 1, -1, -1):
            if obstacleGrid[row][-1] == 1: has_obstacle_in_last_col = True
            if has_obstacle_in_last_col: continue
            dp[row][-1] = 1

        for row in range(len(obstacleGrid) - 2, -1, -1):
            for col in range(len(obstacleGrid[row]) - 2, -1, -1):
                if obstacleGrid[row][col] == 1: continue
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]

        return dp[0][0]