from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filtered = []
        for num in nums:
            if num == val: continue
            filtered.append(num)

        for i in range(len(filtered)): nums[i] = filtered[i]
        for i in range(len(filtered), len(nums)): nums[i] = -1
        return len(filtered)