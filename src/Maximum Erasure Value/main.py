from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        answer = total = left = 0
        appeared: set[int] = set()
        for right in range(len(nums)):
            while nums[right] in appeared:
                total -= nums[left]
                appeared.remove(nums[left])
                left += 1
            total += nums[right]
            appeared.add(nums[right])
            answer = max(total, answer)
        return answer
