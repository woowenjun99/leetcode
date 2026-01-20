from heapq import heapify, heappop
from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = [-x for x in happiness]
        heapify(happiness)
        answer = 0
        for i in range(k): answer += max(-heappop(happiness) - i, 0)
        return answer
