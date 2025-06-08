from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []
        for a in range(1, 10):
            a_current = a
            if a_current > n: break
            answer.append(a_current)
            for b in range(10):
                b_current = a_current * 10 + b
                if b_current > n: break
                answer.append(b_current)
                for c in range(10):
                    c_current = b_current * 10 + c
                    if c_current > n: break
                    answer.append(c_current)
                    for d in range(10):
                        d_current = c_current * 10 + d
                        if d_current > n: break
                        answer.append(d_current)
                        for e in range(10):
                            e_current = d_current * 10 + e
                            if e_current > n: break
                            answer.append(e_current)
        return answer
