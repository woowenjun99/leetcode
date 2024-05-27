from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mappers = { key: 0 for key in range(1, len(nums) + 1) }
        for num in nums: mappers[num] += 1
        answer = [0, 0]
        for key in mappers:
            if mappers[key] == 2: answer[0] = key
            elif mappers[key] == 0: answer[1] = key
        return answer