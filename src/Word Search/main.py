from typing import List

class Solution:
    def dfs(self, board: List[List[str]], visited: List[List[bool]], row: int, col: int, index: int, word: str):
        if index == len(word): return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]): return False
        if visited[row][col] or board[row][col] != word[index]: return False
        visited[row][col] = True
        up = self.dfs(board, visited, row - 1, col, index + 1, word)
        down = self.dfs(board, visited, row + 1, col, index + 1, word)
        left = self.dfs(board, visited, row, col - 1, index + 1, word)
        right = self.dfs(board, visited, row, col + 1, index + 1, word)
        visited[row][col] = False
        return up or down or left or right

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                visited = [[False] * len(board[0]) for _ in range(len(board))]
                if self.dfs(board, visited, row, col, 0, word): return True
        return False