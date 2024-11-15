from heapq import heappush, heappop
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for num in nums:
            heappush(self.pq, num)
            if len(self.pq) > self.k: heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k: heappop(self.pq)
        return self.pq[0]