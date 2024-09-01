from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        return counter["L"] == counter["R"] and counter["U"] == counter["D"]