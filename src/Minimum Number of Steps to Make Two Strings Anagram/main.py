from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = defaultdict(int)
        for letter in s: counter_s[letter] += 1
        for letter in t: counter_s[letter] -= 1
        return sum([value for value in counter_s.values() if value > 0])
