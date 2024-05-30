from typing import List
from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        pq = [(counter[key], key) for key in counter]
        heapify(pq)
        for _ in range(k):
            occurrence, value = heappop(pq)
            occurrence -= 1
            if occurrence > 0: heappush(pq, (occurrence, value))
        return len(pq)