class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            state = guess(mid)
            if state == 0: return mid
            elif state == -1: high = mid - 1
            else: low = mid + 1