from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ids = sorted(set(map(lambda x: x[0], nums1)).union(set(map(lambda x: x[0], nums2))))
        nums1 = { id: val for id, val in nums1 }
        nums2 = { id: val for id, val in nums2 }
        answer = []
        for id in ids:
            num1 = nums1.get(id, 0)
            num2 = nums2.get(id, 0)
            answer.append([id, num1 + num2])
        return answer