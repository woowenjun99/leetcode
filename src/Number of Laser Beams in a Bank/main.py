from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        num_lasers = answer = 0
        for layer in bank:
            num_lasers_present = layer.count("1")
            if not num_lasers_present: continue
            answer += num_lasers_present * num_lasers
            num_lasers = num_lasers_present
        return answer