from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float("inf")
        for length in range(l, r + 1):
            for i in range(len(nums) - length + 1):
                total = sum(nums[i : i + length])
                if total <= 0: continue
                answer = min(answer, total)
        return answer if answer != float("inf") else -1