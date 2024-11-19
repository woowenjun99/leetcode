from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_house = two_house_back = 0
        for num in nums: previous_house, two_house_back = max(previous_house, num + two_house_back), previous_house
        return previous_house
