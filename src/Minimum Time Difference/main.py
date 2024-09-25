from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        visited = [False] * 1440
        min_representation = []
        for timePoint in timePoints:
            hour, minute = list(map(int, timePoint.split(":")))
            if visited[60 * hour + minute]: return 0
            visited[60 * hour + minute] = True
            min_representation.append(60 * hour + minute)
        min_representation.sort()
        answer = float("inf")
        for i in range(len(min_representation) - 1):
            answer = min(answer, min_representation[i + 1] - min_representation[i])
        
        return min(answer, min_representation[0] + 1440 - min_representation[-1])