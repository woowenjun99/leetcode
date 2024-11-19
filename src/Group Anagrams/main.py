from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappers = defaultdict(list)
        for word in strs: mappers["".join(sorted(word))].append(word)
        return list(mappers.values())
