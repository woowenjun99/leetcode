from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        stack = [prices[0]]
        answer = 0
        for i in range(1, len(prices)):
            if stack[-1] - prices[i] == 1: 
                stack.append(prices[i])
                continue
            answer += len(stack) * (len(stack) + 1) // 2
            stack = [prices[i]]
        return answer