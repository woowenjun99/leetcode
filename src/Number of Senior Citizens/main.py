from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = list(map(lambda x: int(x[11:13]), details))
        return len(list(filter(lambda x: x > 60, ages)))
