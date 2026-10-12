class Solution:
    def shortest_distance(self, c: str, current: int):
        left = right = 0
        left_start = right_start = int(c)
        while left_start != current:
            left_start = (left_start - 1) % 10
            left += 1
        while right_start != current:
            right_start = (right_start + 1) % 10
            right += 1
        return min(left, right)

    def minRotations(self, n: int, s: str) -> int:
        total = current = 0
        scores = [0] * len(s)
        for index, c in enumerate(s):
            scores[index].append((self.shortest_distance(c, current), self.shortest_distance(s[-1], current)))
            total += scores[index][0]
            current = int(c)

        improvement = 0
        for score in scores:
            if score[0] <= score[1]: continue
            improvement = max(improvement, score[0] - score[1])
        return total - improvement 