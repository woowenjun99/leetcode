from collections import deque

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        s = deque(s)
        goal = deque(goal)
        for _ in range(len(s)):
            s.append(s.popleft())
            if s == goal: return True
        return False