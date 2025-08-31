from typing import List, Optional

class Solution:
    def __compute_distance(self, colors: List[int], start: int, end: int, step: int):
        shortest: dict[int, int] = {}
        distances: List[List[Optional[int]]] = []
        for index in range(start, end, step):
            color = colors[index]
            distance = [shortest.get(1), shortest.get(2), shortest.get(3)]
            distance[colors[index] - 1] = index
            distances.append(distance)
            shortest[color] = index
        return distances

    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        left_distances: List[List[Optional[int]]] = self.__compute_distance(colors, 0, len(colors), 1)
        right_distances: List[List[Optional[int]]] = self.__compute_distance(colors, len(colors) - 1, -1, -1)[::-1]
        answer: List[int] = []
        for index, color in queries:
            if left_distances[index][color - 1] is None and right_distances[index][color - 1] is None:
                answer.append(-1)
                continue
            if left_distances[index][color - 1] is None:
                answer.append(abs(index - right_distances[index][color - 1]))
                continue
            if right_distances[index][color - 1] is None:
                answer.append(abs(index - left_distances[index][color - 1]))
                continue
            answer.append(min(abs(index - right_distances[index][color - 1]), abs(index - left_distances[index][color - 1])))
        return answer