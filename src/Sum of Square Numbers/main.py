from math import ceil

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = ceil(c ** 0.5)
        while left <= right:
            total = left ** 2 + right ** 2
            if total == c: return True
            elif total < c: left += 1
            else: right -= 1
        return False