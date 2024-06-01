from typing import List

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        common_elements = set(arrays[0])
        for i in range(len(arrays)): common_elements = common_elements.intersection(set(arrays[i]))
        return sorted(common_elements)