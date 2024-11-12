from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[1] * i for i in range(1, rowIndex + 2)]
        for row in range(2, len(answer)):
            for col in range(1, len(answer[row]) - 1):
                answer[row][col] = answer[row - 1][col - 1] + answer[row - 1][col]
        return answer[-1]
