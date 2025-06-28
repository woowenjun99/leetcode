from bisect import bisect_right
from collections import deque
from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums: deque = deque(nums)
        answer = 0
        while nums:
            br = bisect_right(nums, target - nums[0])
            if br != 0: answer += 2 ** (br - 1)
            nums.popleft()
        return answer %  (10**9 + 7)
