from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            has_left = mid - 1 >= 0 and nums[mid - 1] == nums[mid]
            has_right = mid + 1 < len(nums) and nums[mid + 1] == nums[mid]
            if not has_left and not has_right: return nums[mid]
            if (mid % 2 == 0 and has_left) or (mid % 2 == 1 and has_right): right = mid - 1
            else: left = mid + 1