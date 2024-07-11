from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]

        def dfs(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != start or image[row][col] == color: return
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        dfs(sr, sc)
        return image