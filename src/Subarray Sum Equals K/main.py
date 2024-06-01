from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        prefix_sum = answer = 0
        for num in nums:
            prefix_sum += num
            answer += prefix_sums[prefix_sum - k]
            prefix_sums[prefix_sum] += 1
        return answer