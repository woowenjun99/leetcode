from heapq import heappush, heappushpop
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x, y in points: 
            if len(pq) < k: heappush(pq, (-x ** 2 - y ** 2, (x, y)))
            else: heappushpop(pq)
        return [v[1] for v in pq]