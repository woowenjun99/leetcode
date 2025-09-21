from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 != 0: return []
        first = (num - 3) // 3
        return [first, first + 1, first + 2]