from collections import List

class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        selected = ranks[0]
        num_replacement = 0
        for i in range(1, len(ranks)):
            if ranks[i] >= selected: continue
            num_replacement += 1
            selected = ranks[i]
        return num_replacement