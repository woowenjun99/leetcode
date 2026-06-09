from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa = [False] * len(A)
        sb = [False] * len(A)
        answer = []
        count = 0
        for a, b in zip(A, B):
            a -= 1
            b -= 1
            sa[a] = True
            sb[b] = True
            if sb[a]:
                sa[a] = False
                sb[a] = False
                count += 1
            if sa[b]:
                sa[b] = False
                sb[b] = False
                count += 1
            answer.append(count)
        return answer

