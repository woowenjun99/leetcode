from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        mappers = {}
        for num in nums:
            count = 0
            start = num
            while start > 0:
                count += start % 2
                start //= 2
            mappers[num] = count

        sorted_nums = sorted(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums) - 1):
                if mappers[nums[j]] == mappers[nums[j + 1]] and nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums == sorted_nums