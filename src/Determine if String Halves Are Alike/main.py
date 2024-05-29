from collections import defaultdict

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
        counter_a, counter_b = defaultdict(int), defaultdict(int)
        for letter in a:
            if letter.lower() in {"a", "e", "i", "o", "u"}:
                counter_a[letter.lower()] += 1
        for letter in b:
            if letter.lower() in {"a", "e", "i", "o", "u"}:
                counter_b[letter.lower()] += 1
        return sum(counter_a.values()) == sum(counter_b.values())