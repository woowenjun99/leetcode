class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        answer = 0
        for x in range(1, 200):
            if abs(n - x) <= k and (n & x) == 0:
                answer += x
        return answer