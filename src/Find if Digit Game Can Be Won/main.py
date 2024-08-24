from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_of_single_digits = sum_of_double_digits = 0
        for num in nums:
            if num < 10: sum_of_single_digits += num
            else: sum_of_double_digits += num
        return sum_of_single_digits != sum_of_double_digits