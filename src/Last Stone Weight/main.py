from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapify(pq)
        while len(pq) > 1:
            heaviest = -heappop(pq)
            second_heaviest = -heappop(pq)
            if heaviest == second_heaviest: continue
            heappush(pq, -heaviest + second_heaviest)
        return -pq[0] if pq else 0