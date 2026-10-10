from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum_so_far = float("inf")
        indices = [-1, -1]
        maximum_so_far = float("-inf")
        for index, num in enumerate(nums):
            if num > maximum_so_far:
                maximum_so_far = num
                indices[0] = index
            if num < minimum_so_far:
                minimum_so_far = num
                indices[1] = index
        indices.sort()
        return min(indices[1] + 1, len(nums) - indices[0], indices[0] + len(nums) - indices[1] + 1)
