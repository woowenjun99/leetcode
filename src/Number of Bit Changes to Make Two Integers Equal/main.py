class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n: return -1
        answer = 0
        while n > 0:
            if n & 1 == 0 and k & 1 == 1: return -1
            if n & 1 == 1 and k & 1 == 0: answer += 1
            n //= 2
            k //= 2
        return answer