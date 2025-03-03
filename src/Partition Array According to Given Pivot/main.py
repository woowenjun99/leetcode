from collections import deque
from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums_smaller_than_pivot = deque()
        nums_equal_to_pivot = deque()
        nums_greater_than_pivot = deque()
        for num in nums:
            if num < pivot: nums_smaller_than_pivot.append(num)
            elif num == pivot: nums_equal_to_pivot.append(num)
            else: nums_greater_than_pivot.append(num)
        while nums_equal_to_pivot: nums_smaller_than_pivot.append(nums_equal_to_pivot.popleft())
        while nums_greater_than_pivot: nums_smaller_than_pivot.append(nums_greater_than_pivot.popleft())
        return list(nums_smaller_than_pivot)
