from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        response = set()
        for i in range(len(nums) - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    response.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                    left += 1
                    continue
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                    continue
                right -= 1

        return list(response)