class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        total = sum(nums) - nums[-1]
        product = 1
        for index in range(len(nums) - 1, -1, -1):
            if total == product: return index
            total -= nums[index - 1]
            product *= nums[index]
            if total < product: return -1 # Optimisation