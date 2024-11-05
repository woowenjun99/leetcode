class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] not in used:
                    hashmap[s[i]] = t[i]
                    used.add(t[i])
                    continue
                return False
            if hashmap[s[i]] != t[i]: return False
        return True