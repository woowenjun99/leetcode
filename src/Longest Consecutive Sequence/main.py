from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        appeared = set(nums)
        answer = 0
        for num in nums:
            if num - 1 in appeared: continue
            streak = 1
            while num + 1 in appeared:
                streak += 1
                num += 1
            answer = max(answer, streak)
        return answer