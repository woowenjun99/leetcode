from collections import deque
from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        queue = deque(sorted(nums))
        for _ in range(len(nums)):
            queue.append(queue.popleft())
            if list(queue) == nums: return True
        return False
