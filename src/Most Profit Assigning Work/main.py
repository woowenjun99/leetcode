from typing import List
from bisect import bisect_right

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combined = sorted(zip(difficulty, profit))
        profit = [val[1] for val in combined]
        difficulty = [val[0] for val in combined]
        for i in range(1, len(profit)): profit[i] = max(profit[i], profit[i - 1])
        answer = 0
        for w in worker:
            if w < difficulty[0]: continue
            answer += profit[bisect_right(difficulty, w) - 1]
        return answer