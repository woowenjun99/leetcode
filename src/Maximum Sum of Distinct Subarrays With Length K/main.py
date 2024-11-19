from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        answer = window_sum = 0
        for i in range(k):
            window[nums[i]] += 1
            window_sum += nums[i]
        for i in range(len(nums) - k):
            if len(window.keys()) == k: answer = max(window_sum, answer)
            window[nums[i]] -= 1
            window_sum -= nums[i]
            if window[nums[i]] == 0: del window[nums[i]]
            window[nums[i + k]] += 1
            window_sum += nums[i + k]
        return max(window_sum, answer) if len(window.keys()) == k else answer