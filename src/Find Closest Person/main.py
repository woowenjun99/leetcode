class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) == abs(y - z): return 0
        return 1 if abs(x - z) < abs(y - z) else 2
