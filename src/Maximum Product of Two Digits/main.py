from collections import Counter

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = Counter(str(n))
        keys = sorted(digits.keys())
        if digits[keys[-1]] > 1: return int(keys[-1]) * int(keys[-1])
        return int(keys[-1]) * int(keys[-2])