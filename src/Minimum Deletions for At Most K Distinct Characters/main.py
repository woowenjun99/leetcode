from collections import Counter
from heapq import heapify, heappop

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = Counter(s)
        pq = list(counter.values())
        heapify(pq)
        answer = 0
        while len(pq) > k: answer += heappop(pq)
        return answer