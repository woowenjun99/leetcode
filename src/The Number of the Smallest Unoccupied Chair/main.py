from heapq import heappop, heapify, heappush
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        logs = []
        for index, (start, end) in enumerate(times):
            logs.append((start, 1, index))
            logs.append((end, 0, index))
        heapify(logs)
        chairs_sat_on = {}
        pq = list(range(len(times)))
        while True:
            _, is_arrival, number = heappop(logs)
            if number == targetFriend and is_arrival: return heappop(pq)
            if not is_arrival: 
                heappush(pq, chairs_sat_on[number])
                continue
            chairs_sat_on[number] = heappop(pq)