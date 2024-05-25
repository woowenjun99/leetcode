from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = max_so_far = 0
        right = 1
        while left < len(prices) and right < len(prices):
            if prices[right] < prices[left]: left = right
            else: max_so_far = max(max_so_far, prices[right] - prices[left])
            right += 1
        return max_so_far