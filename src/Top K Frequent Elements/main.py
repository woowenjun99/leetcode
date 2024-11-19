from collections import Counter
from heapq import heappush, heappop
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pq = []
        for key, value in counter.items():
            heappush(pq, (value, key))
            if len(pq) > k: heappop(pq)
        return list(map(lambda x: x[1], pq))
