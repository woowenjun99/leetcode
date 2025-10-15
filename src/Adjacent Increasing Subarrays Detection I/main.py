from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            subarray_one = nums[i:i + k]
            if i + k >= len(nums): return False
            subarray_two = nums[i + k: i + 2 * k]
            if sorted(subarray_one) == subarray_one and len(set(subarray_one)) == k and sorted(subarray_two) == subarray_two and len(set(subarray_two)) == k: return True
        return False