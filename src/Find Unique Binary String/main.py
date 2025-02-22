from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        candidates = set(nums)
        for i in range(2 ** len(nums)):
            binary = "0" * (len(nums) - len(bin(i)[2:])) + bin(i)[2:]
            if binary in candidates: continue
            return binary