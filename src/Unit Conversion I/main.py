from collections import defaultdict, deque
from typing import List

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for source, target, factor in conversions: graph[source].append((target, factor))
        distances = { 0: 1 }
        queue = deque([(0, 1)])
        while queue:
            source, current = queue.popleft()
            for target, factor in graph[source]:
                distances[target] = (current * factor) % (10 ** 9 + 7)
                queue.append((target, distances[target]))
        answer = []
        for i in range(len(conversions) + 1): answer.append(distances[i])
        return answer
