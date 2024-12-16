from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def __calculate_gain(self, passed: int, total: int):
        return ((passed + 1) / (total + 1)) - (passed / total)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq = [(-self.__calculate_gain(c[0], c[1]), c[0], c[1]) for c in classes]
        heapify(pq)
        for _ in range(extraStudents):
            _, students_passed, total = heappop(pq)
            heappush(pq, (-self.__calculate_gain(students_passed + 1, total + 1), students_passed + 1, total + 1))
        answer = 0
        for c in pq: answer += c[1] / c[2]
        return answer / len(classes)