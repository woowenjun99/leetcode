from collections import Counter
from math import factorial

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        first = Counter()
        current = n
        f = 0
        while current > 0:
            f += factorial(current % 10)
            first[current % 10] += 1
            current //= 10

        second = Counter()
        while f > 0:
            second[f % 10] += 1
            f //= 10
        return first == second