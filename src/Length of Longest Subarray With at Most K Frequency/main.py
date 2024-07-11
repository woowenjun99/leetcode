from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = right = answer = 0
        counter = defaultdict(int)
        while right < len(nums):
            counter[nums[right]] += 1
            while counter[nums[right]] > k: 
                counter[nums[left]] -= 1
                left += 1
            answer = max(answer, right - left + 1)
            right += 1
        return answer