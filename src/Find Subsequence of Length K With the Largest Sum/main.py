from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        pq = []
        for num in nums:
            heappush(pq, num)
            if len(pq) > k: heappop(pq)
        counter = defaultdict(int)
        for num in pq: counter[num] += 1
        answer = []
        for num in nums:
            if counter[num]:
                answer.append(num)
                counter[num] -= 1
        return answer
