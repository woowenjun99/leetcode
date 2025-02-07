from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = count = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count = nums[i]
                continue
            count += nums[i]
            answer = max(answer, count)
        return answer
