from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        partitions = [[]]
        for index in range(len(nums)):
            if len(partitions[-1]) == 3: partitions.append([])
            partitions[-1].append(nums[index])
        for partition in partitions:
            if partition[2] - partition[0] <= k: continue
            return []
        return partitions