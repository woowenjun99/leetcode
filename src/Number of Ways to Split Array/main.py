from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_of_left_window = nums[0]
        sum_of_right_window = sum(nums) - nums[0]
        answer = 1 if sum_of_left_window >= sum_of_right_window else 0
        for index in range(len(nums) - 2):
            sum_of_left_window += nums[index + 1]
            sum_of_right_window -= nums[index + 1]
            answer += 1 if sum_of_left_window >= sum_of_right_window else 0
        return answer