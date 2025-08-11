from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers: List[int] = []
        power = 0
        MOD = 10 ** 9 + 7
        while n > 0:
            if n % 2 == 1: powers.append(2 ** power)
            n //= 2
            power += 1

        prefix_power = [powers[0]]
        for i in range(1, len(powers)): prefix_power.append(powers[i] * prefix_power[-1])

        answer: List[int] = []
        for query in queries:
            if query[0] == query[1]: 
                answer.append((powers[query[0]]) % MOD)
                continue
            elif query[0] == 0:
                answer.append(prefix_power[query[1]] % MOD)
                continue
            answer.append((prefix_power[query[1]] // prefix_power[query[0] - 1]) % MOD)
        return answer
