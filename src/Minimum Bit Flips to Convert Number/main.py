class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = 0
        while start and goal:
            if start & 1 != goal & 1:
                answer += 1
            start >>= 1
            goal >>= 1
        while start:
            if start & 1 == 1: answer += 1
            start >>= 1
        while goal:
            if goal & 1 == 1: answer += 1
            goal >>= 1
        return answer