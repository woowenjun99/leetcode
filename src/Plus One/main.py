from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] <= 9: break
            digits[i - 1] += 1
            digits[i] %= 10
        if digits[0] >= 10:
            digits[0] %= 10
            return [1] + digits
        return digits