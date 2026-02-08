from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        answer = 0
        total = sum(nums)
        for i in range(len(nums) - 1):
            total -= nums[i]
            count = len(nums) - i - 1
            average = total / count
            answer += 1 if nums[i] > average else 0
        return answer
