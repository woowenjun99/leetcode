class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        substring = count = 0
        for c in s:
            substring += 1
            count += ord(c) - ord("a")
            if substring < k: continue
            result += chr(count % 26 + ord("a"))
            count = substring = 0
        return result
