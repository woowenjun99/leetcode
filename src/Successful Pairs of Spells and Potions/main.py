from bisect import bisect_left
from math import ceil
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer: List[int] = []
        for spell in spells:
            min_potion = ceil(success / spell)
            index = bisect_left(potions, min_potion)
            answer.append(len(potions) - index)
        return answer
