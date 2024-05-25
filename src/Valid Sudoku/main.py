from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check horizontally
        for row in range(9):
            used = [False] * 9
            for col in range(9):
                if board[row][col] == ".": continue
                if used[int(board[row][col]) - 1]: return False
                used[int(board[row][col]) - 1] = True

        # Check vertically
        for col in range(9):
            used = [False] * 9
            for row in range(9):
                if board[row][col] == ".": continue
                if used[int(board[row][col]) - 1]: return False
                used[int(board[row][col]) - 1] = True

        for row in range(3):
            for col in range(3):
                used = [False] * 9
                for i in range(3 * row, 3 * row + 3):
                    for j in range(3 * col, 3 * col + 3):
                        if board[i][j] == ".": continue
                        if used[int(board[i][j]) - 1]: return False
                        used[int(board[i][j]) - 1] = True
        return True