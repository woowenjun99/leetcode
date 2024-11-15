from collections import defaultdict
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_element = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]: next_greater_element[stack.pop()] = num
            stack.append(num)
        answer = []
        for num in nums1: answer.append(next_greater_element[num])
        return answer