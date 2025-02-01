from collections import defaultdict
from typing import List

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums[:k]: counter[num] += 1

        answer = []
        for i in range(len(nums) - k):
            answer.append(len(counter))
            counter[nums[i]] -= 1
            if counter[nums[i]] == 0: del counter[nums[i]]
            counter[nums[i + k]] += 1

        return answer + [len(counter)]