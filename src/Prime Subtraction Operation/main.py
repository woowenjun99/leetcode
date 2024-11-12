from typing import List

class Solution:
    def __generatePrimes(self) -> int:
        bs = [True] * 1001
        bs[0] = bs[1] = False
        for i in range(2, 1001):
            if not bs[i]: continue
            for j in range(i * i, 1001, i):
                bs[j] = False

        prime = []
        for index in range(1001):
            if not bs[index]: continue
            prime.append(index)
        return prime

    def __is_sorted(self, nums: List[int]):
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]: continue
            return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        prime_numbers = self.__generatePrimes()
        for i in range(len(nums)):
            target = nums[0] if i == 0 else nums[i] - nums[i - 1]
            for j in range(len(prime_numbers) - 1, -1, -1):
                if prime_numbers[j] >= target: continue
                nums[i] -= prime_numbers[j]
                break
        return self.__is_sorted(nums)