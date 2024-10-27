from collections import defaultdict
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        running_sum = answer = 0
        cache = defaultdict(int)
        cache[0] = -1
        for index, num in enumerate(nums):
            running_sum += num
            if running_sum - k in cache: answer = max(answer, index - cache[running_sum - k])
            if running_sum not in cache: cache[running_sum] = index
        return answer
