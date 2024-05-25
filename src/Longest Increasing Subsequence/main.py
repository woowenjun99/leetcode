from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sequences = []
        for num in nums:
            if not sequences or num > sequences[-1]: sequences.append(num)
            else:
                index = bisect_left(sequences, num)
                if index < len(sequences): sequences[index] = num
        return len(sequences)