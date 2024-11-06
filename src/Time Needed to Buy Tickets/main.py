from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = list(map(lambda ticket: (ticket, False), tickets))
        tickets[k] = (tickets[k][0], True)
        queue = deque(tickets)
        time = 0
        while True:
            time += 1
            count, is_result = queue.popleft()
            if count == 1 and is_result: return time
            if count > 1: queue.append((count - 1, is_result))