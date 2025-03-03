from collections import deque
from typing import List
from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = deque(sorted(zip(capital, list(map(lambda x: -x, profits)))))
        pq = []
        for _ in range(k):
            while pairs and pairs[0][0] <= w: heappush(pq, pairs.popleft()[1])
            if not pq: return w
            w -= heappop(pq)
        return w