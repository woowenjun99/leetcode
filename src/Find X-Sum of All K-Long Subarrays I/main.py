from collections import defaultdict
from heapq import heappush, heappop
from typing import List, Tuple

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer: List[int] = []
        for i in range(len(nums) - k + 1):
            counter: defaultdict[int, int] = defaultdict(int)
            for j in range(i, i + k): counter[nums[j]] += 1
            pq: List[Tuple[int, int]] = []
            for key, value in counter.items(): heappush(pq, (-value, -key))
            count = popped = 0
            while pq and popped < x:
                value, key = heappop(pq)
                count += -value * -key
                popped += 1
            answer.append(count)
        return answer
