from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mappers = [0] * 33
        for num in nums:
            count = 0
            while num > 0:
                mappers[count] += num % 2
                num //= 2
                count += 1

        answer = 0
        for i in range(k):
            count = 0
            for j in range(len(mappers) - 1, -1, -1):
                if mappers[j] > 0:
                    count = count * 2 + 1
                    mappers[j] -= 1
                else: count *= 2
            answer = (answer + count ** 2) % (10 ** 9 + 7)
        return answer