from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_house = two_house_back = 0
        for current in nums:
            max_amount = max(two_house_back + current, previous_house)
            previous_house, two_house_back = max_amount, previous_house
        return max(previous_house, two_house_back)