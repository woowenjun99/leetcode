from heapq import heappush, heappop
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        timings = [[float("inf")] * len(moveTime[0]) for _ in range(len(moveTime))]
        timings[0][0] = 0
        while pq:
            time, row, col = heappop(pq)
            for direction in directions:
                if 0 <= row + direction[0] < len(moveTime) and 0 <= col + direction[1] < len(moveTime[0]):
                    if time < moveTime[row + direction[0]][col + direction[1]]:
                        timings[row + direction[0]][col + direction[1]] = moveTime[row + direction[0]][col + direction[1]] + 1
                        heappush(pq, (timings[row + direction[0]][col + direction[1]], row + direction[0], col + direction[1]))
                        continue
                    if timings[row + direction[0]][col + direction[1]] > time + 1:
                        timings[row + direction[0]][col + direction[1]] = time + 1
                        heappush(pq, (time + 1, row + direction[0], col + direction[1]))
        return timings[-1][-1]
