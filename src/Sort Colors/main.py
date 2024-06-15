from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
            elif nums[mid] == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
                mid -= 1
            mid += 1