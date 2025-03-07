from typing import List

class Solution:
    def __sieve(self, lower_bound: int, upper_bound: int) -> List[int]:
        sieve_size = upper_bound + 1
        bs = [True] * sieve_size
        bs[0] = bs[1] = False
        primes = []
        for i in range(2, sieve_size):
            if not bs[i]: continue # Is processed before
            for j in range(i * i, sieve_size, i): bs[j] = False
            if lower_bound <= i <= upper_bound: primes.append(i)
        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.__sieve(left, right)
        if len(primes) <= 1: return [-1, -1]
        answer = [primes[0], primes[1]]
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] >= answer[1] - answer[0]: continue
            answer = [primes[i - 1], primes[i]]
        return answer
