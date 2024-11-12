from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        answer = []
        for index, num in enumerate(nums):
            stack = []
            if num == 0:
                answer.append((mapping[0], index))
                continue
            while num > 0:
                stack.append(mapping[num % 10])
                num //= 10
            x = 0
            while stack: x = x * 10 + stack.pop()
            answer.append((x, index))
        return list(map(lambda x: nums[x[1]], sorted(answer)))