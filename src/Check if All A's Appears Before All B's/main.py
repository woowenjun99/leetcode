class Solution:
    def checkString(self, s: str) -> bool:
        return "".join(sorted(list(s))) == s