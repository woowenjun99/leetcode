class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999) + max(0, n - 999999) + max(0, n - 999999999) + max(0, n - 999999999999) + max(0, n - 999999999999999)
