from collections import defaultdict

class Solution:
    def clearStars(self, s: str) -> str:
        mappers = defaultdict(list)
        for i, c in enumerate(s):
            if c != "*":
                mappers[c].append(i)
                continue
            for i in range(26):
                if mappers[chr(ord("a") + i)]:
                    mappers[chr(ord("a") + i)].pop()
                    break
        result = []
        for i in range(26):
            for j in range(len(mappers[chr(ord("a") + i)])):
                result.append((mappers[chr(ord("a") + i)][j], chr(ord("a") + i)))
        result.sort()
        return "".join(map(lambda x: x[1], result))