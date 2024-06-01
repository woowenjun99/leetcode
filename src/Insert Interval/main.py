from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        answer = []
        for interval in intervals:
            if not answer or answer[-1][1] < interval[0]: 
                answer.append(interval)
                continue
            answer[-1] = [min(interval[0], answer[-1][0]), max(interval[1], answer[-1][1])]
        return answer