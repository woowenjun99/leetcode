from collections import deque
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer, stacks = deque(), [[]]
        for num in nums:
            if not stacks[-1] or stacks[-1][-1] + 1 == num:
                stacks[-1].append(num)
                continue
            stacks.append([num])
        
        for stack in stacks:
            for index in range(len(stack)):
                if index + k <= len(stack):
                    answer.append(stack[index + k - 1])
                else:
                    answer.append(-1)
        for _ in range(k - 1): answer.pop()
        return list(answer)