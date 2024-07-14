from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return [] # No point checking
        p_counter = Counter(p)
        substring_counter = Counter(s[:len(p)])
        left = 0
        answer = []
        for right in range(len(p), len(s)):
            if substring_counter == p_counter: answer.append(left)
            substring_counter[s[left]] -= 1
            substring_counter[s[right]] += 1
            left += 1
        if substring_counter == p_counter: answer.append(left)
        return answer