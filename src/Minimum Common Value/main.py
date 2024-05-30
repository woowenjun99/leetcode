from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0
        while left < len(nums1) and right < len(nums2) and nums1[left] != nums2[right]:
            if nums1[left] < nums2[right]: left += 1
            else: right += 1
        if left < len(nums1) and right < len(nums2) and nums1[left] == nums2[right]: return nums1[left]
        return -1