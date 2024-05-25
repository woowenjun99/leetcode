from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        for num in nums:
            maximum_that_can_be_robbed = max(num + rob2, rob1)
            rob1, rob2 = maximum_that_can_be_robbed, rob1
        return rob1