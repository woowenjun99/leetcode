from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                temps[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return temps