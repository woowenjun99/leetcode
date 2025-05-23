from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i * j) % k != 0 or nums[i] != nums[j]: continue
                answer += 1
        return answer
