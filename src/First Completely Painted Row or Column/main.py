from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [n] * m
        cols = [m] * n
        coordinates = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                coordinates[mat[row][col]] = (row, col)

        for index in range(len(arr)):
            r, c = coordinates[arr[index]]
            rows[r] -= 1
            cols[c] -= 1
            if rows[r] == 0 or cols[c] == 0: return index

        return -1
