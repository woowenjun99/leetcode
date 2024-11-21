from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mappers = {}
        for index, num in enumerate(nums2): mappers[num] = index
        answer = []
        for num in nums1: answer.append(mappers[num])
        return answer