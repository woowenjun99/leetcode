from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        answer = 0
        for num in nums:
            if num < k: return -1
            if num == k: continue
            answer += 1
        return answer