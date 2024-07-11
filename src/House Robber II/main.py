from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        previous_house = two_house_back = next_house = two_house_forward = 0
        for i in range(len(nums) - 1):
            max_amount = max(nums[i] + two_house_back, previous_house)
            two_house_back, previous_house = previous_house, max_amount
    
        for i in range(len(nums) - 1, 0, -1):
            max_amount = max(nums[i] + two_house_forward, next_house)
            two_house_forward, next_house = next_house, max_amount

        return max(two_house_back, previous_house, next_house, two_house_forward)