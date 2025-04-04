from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = float("-inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    answer = max(answer, (nums[i] - nums[j]) * nums[k])
        return max(0, answer)
