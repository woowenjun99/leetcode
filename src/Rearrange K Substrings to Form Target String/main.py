from collections import defaultdict

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        counter = defaultdict(int)
        substring = ""
        for i in range(len(s)):
            substring += s[i]
            if len(substring) == len(s) // k:
                counter[substring] += 1
                substring = ""

        for i in range(len(t)):
            substring += t[i]
            if len(substring) == len(t) // k:
                if counter[substring] == 0: return False
                counter[substring] -= 1
                substring = ""
        return True
