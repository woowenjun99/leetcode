from collections import deque
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        queue = deque()
        answer = 0
        for i in range(len(nums) - 2):
            while queue and queue[0] + 2 < i: queue.popleft()
            if (nums[i] + len(queue)) % 2 == 1: continue
            answer += 1
            queue.append(i)
        for i in range(len(nums) - 2, len(nums)):
            while queue and queue[0] + 2 < i: queue.popleft()
            if (nums[i] + len(queue)) % 2 == 1: continue
            return -1
        return answer
