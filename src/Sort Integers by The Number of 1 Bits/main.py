from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        answer = []
        for num in arr:
            count = 0
            temp = num
            while num > 0:
                count += num & 1
                num >>= 1
            answer.append((count, temp))
        return list(map(lambda x: x[1], sorted(answer)))