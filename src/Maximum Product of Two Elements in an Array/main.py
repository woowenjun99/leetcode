from typing import List
from heapq import heappush, heappop

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            heappush(pq, num)
            if len(pq) > 2: heappop(pq)
        return (pq[0] - 1) * (pq[1] - 1)