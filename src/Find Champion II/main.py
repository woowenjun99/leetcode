from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        appeared = set(range(n))
        for _, v in edges: 
            if v not in appeared: continue
            appeared.remove(v)
        return appeared.pop() if len(appeared) == 1 else -1
