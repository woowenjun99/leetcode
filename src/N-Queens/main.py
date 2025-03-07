from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        board = [["."] * n for _ in range(n)]
        cols = [False] * n
        diagonal = set()
        antidiagonal = set()

        def backtracking(row):
            if row == n:
                ans = []
                for r in range(n): ans.append("".join(board[r]))
                answer.append(ans)
                return
            
            for col in range(n):
                if cols[col] or row - col in antidiagonal or row + col in diagonal: continue
                cols[col] = True
                antidiagonal.add(row - col)
                diagonal.add(row + col)
                board[row][col] = "Q"
                backtracking(row + 1)
                board[row][col] = "."
                cols[col] = False
                antidiagonal.remove(row - col)
                diagonal.remove(row + col)
        backtracking(0)
        return answer