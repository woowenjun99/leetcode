class Solution:
    def dfs(self, row, column, grid: list[list[str]]):
        if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[row]) or grid[row][column] == "0":
            return

        grid[row][column] = "0"
        self.dfs(row + 1, column, grid)
        self.dfs(row - 1, column, grid)
        self.dfs(row, column + 1, grid)
        self.dfs(row, column - 1, grid)

    def numIslands(self, grid: list[list[str]]) -> int:
        res = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1":
                    self.dfs(row, column, grid)
                    res += 1

        return res