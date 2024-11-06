from collections import defaultdict

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        current = colors[0]
        counter = defaultdict(int)
        count = 0
        for color in colors:
            if color == current:
                count += 1
            else:
                counter[current] += max(0, count - 2)
                count = 1
                current = color
        counter[current] += max(0, count - 2)
        return counter["A"] > counter["B"]