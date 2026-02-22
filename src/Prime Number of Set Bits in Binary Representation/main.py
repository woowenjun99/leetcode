class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set()
        _sieve_size = 33
        bs = [True] * 33
        bs[0] = bs[1] = False
        for i in range(2, _sieve_size):
            if bs[i]:
                for j in range(i * i, _sieve_size, i): bs[j] = False
                primes.add(i)

        answer = 0
        for i in range(left, right + 1):
            set_bits = 0
            current = i
            while current > 0:
                set_bits += current % 2
                current //= 2
            if set_bits in primes: answer += 1
        return answer