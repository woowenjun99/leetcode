from collections import deque
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        dq = deque(sorted(people))
        answer = 0
        while dq:
            answer += 1
            if dq[-1] == limit or dq[-1] + dq[0] > limit:
                dq.pop()
                continue
            dq.popleft()
            if dq: dq.pop()
        return answer