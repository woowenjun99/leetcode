from collections import deque
from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shifts = 0
        for direction, amount in shift:
            if direction == 0: shifts -= amount
            else: shifts += amount

        dq = deque(s)
        while shifts != 0:
            if shifts > 0:
                dq.appendleft(dq.pop())
                shifts -= 1
            else:
                dq.append(dq.popleft())
                shifts += 1

        return "".join(dq)