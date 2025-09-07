from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer: List[int] = []
        if n % 2 == 1: 
            answer.append(0)
            n -= 1
        i = 1
        while n > 0:
            answer.append(i)
            answer.append(-i)
            i += 1
            n -= 2
        return answer