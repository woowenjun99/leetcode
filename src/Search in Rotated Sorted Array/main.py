class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            if nums[left] < nums[mid]: # Left subarray is sorted OR entire array is sorted
                if nums[left] <= target <= nums[mid]: right = mid - 1
                else: left = mid + 1
                continue
            if nums[mid] <= target <= nums[right]: left = mid + 1 # Right subarray is sorted
            else: right = mid - 1
        return -1