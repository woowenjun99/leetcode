from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)
        duplicate = code.copy()
        for i in range(len(code)):
            total = 0
            for j in range(1, 1 + abs(k)): total += duplicate[(i - j if k < 0 else i + j) % len(code)]
            code[i] = total
        return code