from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk_used_in_one_round = sum(chalk)
        if total_chalk_used_in_one_round < k:
            k %= total_chalk_used_in_one_round
        idx = 0
        while k >= chalk[idx]:
            k -= chalk[idx]
            idx = (idx + 1) % len(chalk)
        return idx