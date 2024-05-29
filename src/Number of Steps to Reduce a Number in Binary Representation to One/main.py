class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = int(s, 2)
        while s != 1:
            steps += 1
            if s % 2 == 1: s += 1
            else: s = s // 2
        return steps