from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(1, len(points)):
            if points[i][0] == points[i - 1][0] or abs(points[i][0] - points[i - 1][0]) < abs(points[i][1] - points[i - 1][1]): answer += abs(points[i][1] - points[i - 1][1])
            else: answer += abs(points[i][0] - points[i - 1][0])
        return answer
