from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = right = 0

        B = []

        b_index = 0

        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                B.append(nums1[left])
                left += 1
            else:
                B.append(nums2[right])
                right += 1

        while left < m:
            B.append(nums1[left])
            left += 1

        while right < n:
            B.append(nums2[right])
            right += 1

        for k in range(len(B)):
            nums1[k] = B[k]