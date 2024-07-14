from typing import List

class Solution:
    def find_min_index(self, nums):
        min_index = left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                if nums[left] < nums[min_index]: min_index = left
                break
            mid = (left + right) // 2
            if nums[mid] < nums[min_index]: min_index = mid
            if nums[left] <= nums[mid]: left = mid + 1
            else: right = mid - 1 
        return min_index

    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_min_index(nums)
    
        if target >= nums[min_index] and target <= nums[-1]:
            left = min_index
            right = len(nums) - 1
        else:
            left = 0
            right = min_index - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid - 1
            else: left = mid + 1
        return -1