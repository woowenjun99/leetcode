from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = sorted(set(arr))
        ranks = {}
        for i in range(len(unique)): ranks[unique[i]] = i + 1
        for i in range(len(arr)): arr[i] = ranks[arr[i]]
        return arr
