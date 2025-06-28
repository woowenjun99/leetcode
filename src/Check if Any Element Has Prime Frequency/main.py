from collections import Counter
from typing import List

class Solution:
    def __is_prime(self, num: int):
        if num == 1: return False
        for i in range(2, num):
            if num % i == 0: return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        values = list(counter.values())
        for value in values:
            if self.__is_prime(value): return True
        return False