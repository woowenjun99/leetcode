from collections import Counter
from typing import List

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.mappers = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.mappers[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.mappers[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        answer = 0
        for num in self.nums1: answer += self.mappers[tot - num]
        return answer