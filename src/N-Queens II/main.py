class Solution:
    def totalNQueens(self, n: int) -> int:
        answer = 0
        board = [["."] * n for _ in range(n)]
        cols = [False] * n
        diagonal = set()
        antidiagonal = set()

        def backtracking(row):
            nonlocal answer
            if row == n:
                answer += 1
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