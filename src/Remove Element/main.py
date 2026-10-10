from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[right] == val:
                right -= 1
                continue
            if nums[left] != val:
                left += 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        return right + 1