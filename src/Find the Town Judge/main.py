from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outgoing_edges = [0] * n
        incoming_edges = [0] * n
        for a, b in trust:
            outgoing_edges[a - 1] += 1
            incoming_edges[b - 1] += 1
        for i in range(n):
            if incoming_edges[i] == n - 1 and outgoing_edges[i] == 0:
                return i + 1
        return -1