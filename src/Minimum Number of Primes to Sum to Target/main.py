from typing import List

class Solution:
    def __sieve(self, m: int):
        bs = [True] * 1000
        bs[0] = bs[1] = False
        primes = []
        for i in range(2, len(bs)):
            if not bs[i]: continue
            for j in range(i * i, len(bs), i): bs[j] = False
            primes.append(i)
            if len(primes) == m: break
        return primes
    
    def __coin_change(self, n: int, primes: List[int]):
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in primes:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[-1] if dp[-1] != float("inf") else -1

    def minNumberOfPrimes(self, n: int, m: int) -> int:
        primes = self.__sieve(m)
        return self.__coin_change(n, primes)