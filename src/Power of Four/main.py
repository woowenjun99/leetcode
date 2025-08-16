class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        current = 0
        while 4 ** current <= n:
            if 4 ** current == n: return True
            current += 1
        return False