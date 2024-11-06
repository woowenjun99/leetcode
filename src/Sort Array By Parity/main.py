from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = list(filter(lambda num: num % 2, nums))
        even = list(filter(lambda num: num % 2 == 0, nums))
        return even + odd