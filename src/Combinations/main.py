class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        response = []

        def backtracking(start, arr):
            if len(arr) == k:
                response.append(arr.copy())
                return
            
            for i in range(start, n + 1):
                arr.append(i)
                backtracking(i + 1, arr)
                arr.pop()

        backtracking(1, [])
        return response