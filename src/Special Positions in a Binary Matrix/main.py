from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        answer = 0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0 or sum(mat[row]) != 1: continue
                col_sum = 0
                for r in range(len(mat)): col_sum += mat[r][col]
                if col_sum != 1: continue
                answer += 1
        return answer