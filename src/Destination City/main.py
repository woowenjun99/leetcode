from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source, dest = set(), set()
        for a, b in paths:
            source.add(a)
            dest.add(b)
        return dest.difference(source).pop()