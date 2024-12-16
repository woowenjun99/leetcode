from collections import defaultdict, deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = defaultdict(list)
        distances = defaultdict(lambda:float("inf"))
        distances[startGene] = 0
        bank.append(startGene)

        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                difference = left = right = 0
                while left < len(bank[i]):
                    if bank[i][left] != bank[j][right]: difference += 1
                    left += 1
                    right += 1
                if difference == 1:
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])
        
        queue = deque([(startGene, 0)])
        while queue:
            node, distance = queue.popleft()
            for neighbour in graph[node]:
                if distance + 1 < distances[neighbour]:
                    distances[neighbour] = distance + 1
                    queue.append((neighbour, distance + 1))
        return distances[endGene]
