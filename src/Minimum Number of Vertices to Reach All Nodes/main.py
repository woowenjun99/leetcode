from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for u, v in edges: indegrees[v] += 1
        answer = []
        for i in range(len(indegrees)):
            if not indegrees[i]: answer.append(i)
        return answer