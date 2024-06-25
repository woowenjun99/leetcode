from typing import List
from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        answer = 0
        queue = deque()
        for index, num in enumerate(nums):
            while queue and index - queue[0] >= k: queue.popleft()
            if (num + len(queue)) % 2 == 1: continue
            if index + k > len(nums): return -1
            answer += 1
            queue.append(index)
        return answer