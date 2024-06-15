from typing import List
from heapq import heappush, heappop

class Solution:
    def filter_projects(self, projects, pq, profits, w):
        while projects and projects[-1][0] <= w:
            _, index = projects[-1]
            heappush(pq, (-profits[index], index))
            projects.pop()

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted([(capital[i], i) for i in range(len(profits))], reverse=True)
        pq = []
        self.filter_projects(projects, pq, profits, w)

        while k > 0 and pq:
            w += profits[heappop(pq)[1]]
            self.filter_projects(projects, pq, profits, w)
            k -= 1
        
        return w