from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()
        for interval in intervals:
            if not answer or answer[-1][1] < interval[0]: 
                answer.append(interval)
                continue
            answer[-1] = [min(interval[0], answer[-1][0]), max(interval[1], answer[-1][1])]
        return answer