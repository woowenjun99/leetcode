from collections import defaultdict

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1_odd_letters = defaultdict(int)
        s2_odd_letters = defaultdict(int)
        s1_even_letters = defaultdict(int)
        s2_even_letters = defaultdict(int)
        for i in range(1, len(s1), 2):
            s1_odd_letters[s1[i]] += 1
            s2_odd_letters[s2[i]] += 1
        for i in range(0, len(s1), 2):
            s1_even_letters[s1[i]] += 1
            s2_even_letters[s2[i]] += 1
        return s1_odd_letters == s2_odd_letters and s1_even_letters == s2_even_letters
