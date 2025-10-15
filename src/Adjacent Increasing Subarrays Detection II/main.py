from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        subarray_sizes = [1]
        for index in range(1, len(nums)):
            if nums[index] <= nums[index - 1]:
                subarray_sizes.append(1)
                continue
            subarray_sizes[-1] += 1
        
        answer = 0
        for index in range(len(subarray_sizes)):
            candidates = [answer, subarray_sizes[index] // 2]
            if index < len(subarray_sizes) - 1: candidates.append(min(subarray_sizes[index], subarray_sizes[index + 1]))
            answer = max(candidates)
        return answer
