from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        length_of_largest_number = 0
        sorted_nums = nums.copy()
        for num in nums: length_of_largest_number = max(length_of_largest_number, len(num))
        for i in range(len(nums)): sorted_nums[i] = ("0" * (length_of_largest_number - len(nums[i])) + nums[i], i)
        sorted_nums.sort(reverse=True)
        return nums[sorted_nums[k - 1][1]]