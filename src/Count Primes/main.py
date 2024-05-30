class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        _sieve_size = n

        bs = [True] * 10000010
        bs[0] = bs[1] = False
        for i in range(2, _sieve_size):
            if bs[i]:
                for j in range(i * i, _sieve_size, i):
                    bs[j] = False
                primes += 1

        return primes